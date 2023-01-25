from django.urls import include, path, re_path
from . import views
from .views import *

urlpatterns = [
    path('login/', OTPLoginView.as_view(), name='OTPLoginView'),
    path('register/', OTPRegisterView.as_view(), name='OTPRegisterView'),
    path('logout/', User_logout_user, name='logoutclient'),
]
