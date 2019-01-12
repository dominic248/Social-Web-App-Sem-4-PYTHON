from django.urls import path,include
from . import views as registrationviews
from allauth.account.views import EmailView as allauth_AccountEmail



urlpatterns=[
    path('', registrationviews.home, name='home'),
    path('secret/',registrationviews.secret_page,name='secret'),
    path('accounts/email/',allauth_AccountEmail.as_view(),name='account_email'),
    path('accounts/', include('allauth.urls')),

]