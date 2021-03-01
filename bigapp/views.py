from django.shortcuts import render
from django.utils import timezone
from .forms import CustomUserForm, LoginForm, TweetItemForm
from .models import TweetItem, CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def index_view(request):
    tweets = TweetItem.objects.all().order_by('dt_posted').reverse()

    return render(request, 'index.html', {
        'heading': 'Tweet, Tweet, Tweety Tweet...Tweet!',
        'tweets': tweets,
    })


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
            return HTTPResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'general_form.html', {
        'heading': 'Login Here',
        'form': form,
        })