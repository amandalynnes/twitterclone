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


def add_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                title=data['title'],
                body=data['body'],
                # dt_posted=data['dt_posted'],
                posted_by=request.user,
            )
            return HttpResponseRedirect(reverse('tweet', args=([new_tweet.id])))
    form = TweetForm()
    return render(request,
    'general_form.html', {
        'heading': 'Post A Tweet',
        'form': form}
    )



def tweet_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet_view.html', {
        'heading': 'Tweet',
        'tweet': tweet
    })



