from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.conf import settings

# Create your models here.


class TwitterUser(AbstractUser):
    pass
