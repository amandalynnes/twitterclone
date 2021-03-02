from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TwitterUser

# from .models import TwitterUser, Tweet

# Register your models here.

admin.site.register(TwitterUser, UserAdmin)

# admin.site.register(Tweet)

