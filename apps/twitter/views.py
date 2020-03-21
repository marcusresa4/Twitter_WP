from django.shortcuts import render
from apps.twitter.models import Tweet, TwitterUser, Statistics, Impact

def twitter(request):
    tweets = Tweet.objects.all()
    impacts = Impact.objects.all()

    context = { 'tweets' : tweets,
                'impacts' : impacts
    }

    return render(request, 'feed.html', context)

def twitteruser(request, username):
    tweets = Tweet.objects.filter(
        user__username__contains=username)

    user = TwitterUser.objects.filter(
        username__contains=username
    )
    impacts = Impact.objects.all()
    context = {
        'users': user,
        'tweets': tweets,
        'impacts' : impacts
    }

    return render(request, 'tweets_user.html', context)


def twitterhashtag(request, hashtag):
    tweets = Tweet.objects.filter(
        hashtag_in_tweet__hashtag__contains=hashtag)

    impacts = Impact.objects.all()
    context = {
        'hashtag': hashtag,
        'tweets': tweets,
        'impacts' : impacts
    }

    return render(request, 'tweets_hashtag.html', context)

