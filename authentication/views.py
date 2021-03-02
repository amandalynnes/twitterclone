from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from twitteruser.forms import TwitterUserForm
from authentication.forms import LoginForm
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password'],
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'general_form.html', {
        'heading': 'Login Here',
        'form': form,
        })
