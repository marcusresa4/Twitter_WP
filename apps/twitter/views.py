from django.shortcuts import render
from apps.twitter.models import Tweet, TwitterUser, Statistics, Impact, Hashtag
import sys
from . import user_api
from apps.twitter.forms import TweetForm
import random


def twitter(request):
    if request.method == 'POST':
        if "Create Tweet" in request.POST:
            create_tweet(request)

    tweets = Tweet.objects.all()
    impacts = Impact.objects.all()
    form = TweetForm()

    context = { 'tweets'    : tweets,
                'impacts'   : impacts,
                'form'      : form
    }

    return render(request, 'feed.html', context)

def create_tweet(request):
    form = TweetForm(request.POST)
    if form.is_valid():
        created = TwitterUser.objects.all().filter(username="@superuser").count() != 0
        if not created:
            user = TwitterUser.objects.create(
                username="@superuser",
                realname="User Super",
                following=0,
                followers=0,
                profile_picture="img/profilepicture5.jpg",
            )
            user.save()
        else:
            user = TwitterUser.objects.get(username="@superuser")

        tweet = Tweet.objects.create(
            id_tweet=random.randrange(0, 999999999),
            text=form.cleaned_data['text'],
            user=user
        )
        hashtags = create_hashtags(form)
        tweet.hashtag_in_tweet.set(hashtags)
        tweet.save()

def create_hashtags(form):
    hashtag = []
    hashtags_str = form.cleaned_data['hashtag_in_tweet'].split()
    for ht in hashtags_str:
        hashtags, created = Hashtag.objects.get_or_create(hashtag=ht)
        hashtag.append(hashtags)

    return hashtag



def external(request):
    input = request.POST.get('param')
    try:
        output = user_api.get_tweets(input)
    except:
        output = "ERROR!!!!"

    context = {
        'data' : output
    }

    return render(request, 'api.html', context)


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

