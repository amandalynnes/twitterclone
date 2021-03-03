from django import forms
from twitteruser.models import TwitterUser


class LoginForm(forms.Form):
    # email = forms.CharField(widget=forms.EmailInput)
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)


class TwitterUserForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = (
            'username',
            'password',
        )


