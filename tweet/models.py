from django.db import models
from twitteruser.models import TwitterUser
from django.utils.timezone import now


# Create your models here.


class Tweet(models.Model):
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=140)
    dt_posted = models.DateTimeField(default=now)
    posted_by = models.ForeignKey(TwitterUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
