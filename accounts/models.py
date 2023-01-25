from django.db import models

import random
import string
import uuid
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from phone_field import PhoneField
# from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import datetime, timedelta
from extensions.sms_api import send_otp
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class OtpRequestQueryset(models.QuerySet):
    def is_valid(self, phone, request, code):
        current_time = timezone.now()
        return self.filter(
            phone=phone,
            request_id=request,
            code=code,
            create__lt=current_time,
            create__gt=current_time - timedelta(seconds=120),
        ).exists()


class OTPManager(models.Manager):

   
    def get_queryset(self):
        return OtpRequestQueryset(self.model, self._db)

    def is_valid(self, phone, request, code):
        return self.get_queryset().is_valid(phone=phone, request=request, code=code)

    def generate(self, data):
        otp = self.model(phone=data['phone'])
        otp.save(using=self._db)
        send_otp(otp)
        return otp

def generate_otp():
    rand = random.SystemRandom()
    digits = rand.choices(string.digits, k=4)
    return ''.join(digits)


class OTPRequest(models.Model):
    request_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    # name = models.CharField(max_length=50, null=True,verbose_name ='نام')
    phone = models.CharField(max_length=30, null=False ,verbose_name ='تلفن')
    code = models.CharField(max_length=30, default=generate_otp,verbose_name ='کد')
    create = models.DateTimeField(auto_now_add=True, editable=False,verbose_name ='تاریخ ساخت')
    objects = OTPManager()



  

    class Meta:
        verbose_name = 'درخواست otp'
        verbose_name_plural = 'درخواست otp'


