from django import forms
from twitteruser.models import TwitterUser


class LoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = TwitterUser
        fields = ('email', 'password')
