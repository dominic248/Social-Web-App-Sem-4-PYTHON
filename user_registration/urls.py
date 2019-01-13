from django.urls import path,include
from .views import home,secret_page,settings
from allauth.account.views import EmailView as allauth_AccountEmail



urlpatterns=[
    path('', home, name='home'),
    path('secret/',secret_page,name='secret'),
    path('accounts/email/',allauth_AccountEmail.as_view(),name='account_email'),
    path('accounts/', include('allauth.urls')),
    path('settings/', settings, name='settings'),

]