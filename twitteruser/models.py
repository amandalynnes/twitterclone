from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.conf import settings

# Create your models here.


class TwitterUser(AbstractUser):
    pass

class Tweet(models.Model):
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=140)
    dt_posted = models.DateTimeField(default=now)
    posted_by = models.ForeignKey(TwitterUser, null=True, on_delete=models.CASCADE)
    # posted_by = models.ForeignKey(TwitterUser, null=True, on_delete=models.CASCADE, related_name='posted_by')

    def __str__(self):
        return self.title


class Notification(models.Model):
    pass