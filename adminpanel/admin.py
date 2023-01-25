from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django_restful_admin import admin as d


class UserProfileManager(BaseUserAdmin):
    form = UserCreateForm

    list_display = ( 'phone', 'is_admin','is_client', 'is_active')
    list_filter = ('phone', 'is_admin','is_client', 'is_active')
    fieldsets = (
        ('user', {'fields': ('phone', 'password', 'is_client','username')}),
        ('persenal info', {'fields': ('is_admin',)}),
        ('peremissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('phone', 'username','password1', 'password2', 'is_admin','is_client', 'is_active')}),

    )
    search_fields = ('phone', 'username',)
    ordering = ('phone', 'username',)
    filter_horizontal = ()


admin.site.register(User, UserProfileManager)
admin.site.unregister(Group)


