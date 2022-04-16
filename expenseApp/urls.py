from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('signup_page/', signup_page, name="signup_page"),
    path('otp_page/', otp_page, name="otp_page"),
    path('otp_verify/', otp_verify, name="otp_verify"),
    path('signin_page/', signin_page, name="signin_page"),

    path('profile_page/', profile_page, name="profile_page"),
    path('profile_update/', profile_update, name="profile_update"),

    path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('expenses_page/', expenses_page, name="expenses_page"),
    
    path('signout/', signout, name="signout"),
]