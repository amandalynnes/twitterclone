from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.forms import TwitterUserForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/accounts/login/')
def index_view(request):
    tweets = Tweet.objects.all().order_by('dt_posted').reverse()
    notifications = Notification.objects.filter(recipient=request.user)

    return render(request, 'index.html', {
        'heading': 'Tweet, Tweet, Tweety Tweet...Tweet!',
        'tweets': tweets,
        'notifications': notifications,

    })


def user_detail(request, user_id):
    user = TwitterUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(posted_by=user)
    tweets = tweets.order_by('dt_posted').reverse()
    # follow_tweets = Tweet.objects.filter(following)
    count = tweets.count()

    return render(request, 'user_view.html', {
        'user': user,
        'tweets': tweets,
        'count': count,
        })


def edit_user(request, user_id):
    context = {}
    user = TwitterUser.objects.get(id=user_id)

    if request.method == 'POST':
        form = TwitterUserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user.username = data['username']
            user.email = data['email']
            user.save()
            return HttpResponseRedirect(reverse('user_detail', args=[user.id]))

    form = TwitterUserForm(
        initial={'username': user.username, 'email': user.email}
    )
    context.update({
        'user': user,
        'form': form})
    return render(
        request,
        'general_form.html',
        context
        )


@login_required()
def follow_user(request, user_id):
    user = TwitterUser.objects.get(id=user_id)
    follower = TwitterUser.objects.get(id=request.user.id)
    follower.following.add(user)
    follower.save()
    return HttpResponseRedirect(reverse('user_detail', args=[user.id]))


def unfollow_user(request, user_id):
    user = TwitterUser.objects.get(id=user_id)
    follower = TwitterUser.objects.get(id=request.user.id)
    follower.following.remove(user)
    follower.save()
    return HttpResponseRedirect(reverse('user_detail', args=[user.id]))
