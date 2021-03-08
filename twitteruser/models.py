from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.conf import settings

# Create your models here.


class TwitterUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username
