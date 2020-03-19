from django.shortcuts import render
from apps.twitter.models import Tweet, TwitterUser

def twitter(request):
    tweets = Tweet.objects.all()
    context = { 'tweets' : tweets}
    return render(request, 'feed.html', context)

def twitteruser(request, username):
    tweets = Tweet.objects.filter(
        user__username__contains=username)

    user = TwitterUser.objects.filter(
        username__contains=username
    )
    context = {
        'users': user,
        'tweets': tweets
    }

    return render(request, 'tweets_user.html', context)


def twitterhashtag(request, hashtag):
    tweets = Tweet.objects.filter(
        hashtag_in_tweet__hashtag__contains=hashtag)
    context = {
        'hashtag': hashtag,
        'tweets': tweets
    }

    return render(request, 'tweets_hashtag.html', context)

