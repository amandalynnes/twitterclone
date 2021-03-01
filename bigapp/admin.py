from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TweetItem

# Register your models here.

admin.site.register(CustomUser, UserAdmin)

admin.site.register(TweetItem)
