# Generated by Django 3.1.7 on 2021-03-08 18:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0002_auto_20210302_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='following',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
