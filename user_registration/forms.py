from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django import forms

# UserForm,AddEmailForm


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        password1_help_text = '<ul>' \
                              '<li>Your password can\'t be too similar to your other personal information.</li>' \
                              '<li>Your password must contain at least 8 characters.</li>' \
                              '<li>Your password can\'t be a commonly used password.</li>' \
                              '<li>Your password can\'t be entirely numeric.</li>' \
                              '</ul>'
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(max_length=30, required=True, label='First Name',
                                     widget=forms.TextInput(attrs={'placeholder': 'First name'}))
        self.fields['last_name'] = forms.CharField(max_length=30, required=True, label='Last name',
                                    widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
        self.fields['email'] = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.',
                                 label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
        self.fields['username'] = forms.CharField(required=True,
                                   help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                   label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
        self.fields['password1'] = forms.CharField(required=True, help_text=password1_help_text, label='Password',
                                                   widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
        self.fields['password2'] = forms.CharField(required=True, help_text='Enter the same password as before, for verification.',
                                    label='Confirm Password',
                                    widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Add your own processing here.
        # You must return the original result.
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user
    field_order = ['first_name','last_name','email','username','password1','password2']

