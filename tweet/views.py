from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
from re import search

# Create your views here.


def add_tweet(request): 
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                title=data['title'],
                body=data['body'],
                posted_by=request.user,
            )
            match_obj = search(r'@(\w+)', new_tweet.body)
            recipient = match_obj.group(1)
            recipient = TwitterUser.objects.filter(username=recipient).first()

            if recipient and match_obj:
                notification = Notification.objects.create(
                    recipient=recipient,
                    tweet=new_tweet,
                    # read=False,
            )

            return HttpResponseRedirect(reverse('tweet', args=([new_tweet.id])))
    form = TweetForm()
    return render(request, 'general_form.html', {
        'heading': 'Post A Tweet',
        'form': form,
    })


def tweet_view(request, tweet_id):
    if request.user.is_authenticated:
        tweet = Tweet.objects.get(id=tweet_id)
        notifications = Notification.objects.filter(recipient=request.user)

        return render(request, 'tweet_view.html', {
            'heading': 'Tweet',
            'tweet': tweet,
            'notifications': notifications,
        })

    else:
        tweet = Tweet.objects.get(id=tweet_id)

        return render(request, 'tweet_view.html', {
            'heading': 'Tweet',
            'tweet': tweet,
        })


def tweet_edit(request, tweet_id):

    context = {}
    tweet = Tweet.objects.get(id=tweet_id)

    if request.method == 'POST':
        form = TweetForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            tweet.title = data['title']
            tweet.body = data['body']
            tweet.posted_by = request.user
            tweet.save()
            return HttpResponseRedirect(reverse('increment', args=[tweet.id]))

    form = TweetForm(
        initial={'title': tweet.title, 'body': tweet.body, }
    )
    context.update({'form': form})
    return render(
        request,
        'general_form.html',
        context
    )
