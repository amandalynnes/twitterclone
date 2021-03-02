from django import forms
from twitteruser.models import TwitterUser


class TweetForm(forms.Form):
    title = forms.CharField(max_length=40)
    body = forms.CharField(max_length=140)
