import re
from django.db.models.signals import post_save

from django.db import models
from django.urls import reverse
from django.conf import settings
from .validators import validate_blank_content
from hashtags.signals import parsed_hashtags


# Create your models here.
class PostManager(models.Manager):
    def like_toggle(self,user,post_obj):
        if user in post_obj.liked.all():
            is_liked=False
            post_obj.liked.remove(user)
        else:
            is_liked=True
            post_obj.liked.add(user)
        return is_liked


class Post(models.Model):
    objects=PostManager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, validators=[validate_blank_content])
    image=models.ImageField(upload_to="posts",null=True,blank=True,default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="liked")
    


    def __str__(self):
        return (str(self.user.username) + " | " + str(self.id) + " | " + str(self.created_on))

    def get_absolute_url(self):
        return reverse("post:detail",kwargs={"pk":self.pk})

    class Meta:
        ordering=['-updated_on']

def post_save_receiver(sender,instance,created,*args,**kwargs):
    if created:
        user_regex=r'@(?P<username>[\w.@+-]+)'
        usernames = re.findall(user_regex, instance.content)


        hash_regex = r'#(?P<hashtag>[\w\d-]+)'
        hashtags = re.findall(hash_regex, instance.content)
        parsed_hashtags.send(sender=instance.__class__,hashtag_list=hashtags)




post_save.connect(post_save_receiver,sender=Post)