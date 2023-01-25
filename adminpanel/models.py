from django.db import models

import random
import string
import uuid
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from phone_field import PhoneField
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import datetime, timedelta
from extensions.sms_api import send_otp
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_userr(self, phone, password=None):
        if not phone:
            raise ValueError('please enter valid phone')
        user = self.model(phone=phone, password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        user = self.create_userr( phone,password)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_client(self, phone, name):
        user = self.model(phone=phone, name=name)
        user.is_client=True
        user.save(using=self._db)
        return user

    def create_user(self, phone):
        user = self.model(phone=phone)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField( max_length=128, null=True,blank=True,
                                verbose_name ='نام کاربری')
    password = models.CharField(max_length=128, null=True,blank=True,
                                verbose_name ='پسوورد')
    # name = models.CharField(max_length=50, null=True,verbose_name ='نام')
    phone = models.CharField(max_length=30, unique=True,verbose_name ='تلفن')
    is_active = models.BooleanField(default=True,verbose_name ='فعال/غیرفعال')
    is_admin = models.BooleanField(default=False,verbose_name ='ادمین')
    is_client = models.BooleanField(default=False,verbose_name ='کلاینت')
    USERNAME_FIELD = 'phone'

    objects = UserManager()
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

