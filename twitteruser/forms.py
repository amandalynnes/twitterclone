from django import forms
from .models import TwitterUser


class TwitterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = TwitterUser
        fields = ('email', 'username', 'password')


# class LoginForm(forms.ModelForm):
#     email = forms.CharField(widget=forms.EmailInput)
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = TwitterUser
#         fields = ('email', 'password')


# class TweetForm(forms.Form):
#     title = forms.CharField(max_length=40)
#     body = forms.CharField(max_length=140)
