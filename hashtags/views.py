from django.shortcuts import render
from django.views import View

from .models import HashTag

class HashTagView(View):
    def get(self,request,hashtag,*args,**kwargs):
        obj,created=HashTag.objects.get_or_create(tag=hashtag)
        print("Hashtag",created)
        return render(request,'hashtags/tag_view.html',{"obj":obj})
