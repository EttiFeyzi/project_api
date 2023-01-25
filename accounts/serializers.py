from rest_framework import serializers
from .models import OTPRequest




class RequestOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=50, allow_null=False)


class RequestOTPResponseSerilizer(serializers.ModelSerializer):
    class Meta:
        model = OTPRequest
        fields = ['request_id']
        extra_kwargs = {
           
            "request_id": {"required": True},
            
        }


class UserCreationSerilizer(serializers.Serializer):
    request_id = serializers.UUIDField(allow_null=False)
    code = serializers.CharField(max_length=4, allow_null=False)
    phone = serializers.CharField(max_length=65, allow_null=False)
    # name = serializers.CharField(max_length=30)


class ObtainTokenSerilizer(serializers.Serializer):
    token = serializers.CharField(max_length=120, allow_null=False)
    refresh = serializers.CharField(max_length=120, allow_null=False)
    created = serializers.BooleanField()


class VerifyOtpRequestSerilzer(serializers.Serializer):
    request_id = serializers.UUIDField(allow_null=False)
    code = serializers.CharField(max_length=4, allow_null=False)
    phone = serializers.CharField(max_length=65, allow_null=False)


class RequestSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=50, allow_null=False)
    # name = serializers.CharField(max_length=30)

class AdminSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, allow_null=False)
    password = serializers.CharField(max_length=30)

class VerifyRequestSerilzer(serializers.Serializer):
    request_id = serializers.UUIDField(allow_null=False)
    code = serializers.CharField(max_length=4, allow_null=False)