from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile

# Register your models here.

admin.site.register(UserProfile)
