from django.shortcuts import render
from apps.twitter.models import Tweet, TwitterUser, Statistics, Impact, Hashtag
from . import user_api
from apps.twitter.forms import TweetForm
import random


def twitter(request):
    if request.method == 'POST':
        if "Create Tweet" in request.POST:
            create_tweet(request)
        elif "API" in request.POST:
            create_tweet_from_API(request)
        elif "Edit Tweet" in request.POST:
            edit_tweet(request)


    tweets = Tweet.objects.all()
    impacts = Impact.objects.all()
    form = TweetForm()

    context = { 'tweets'    : tweets,
                'impacts'   : impacts,
                'form'      : form
    }

    return render(request, 'feed.html', context)

def edit_tweet(request):
    form = TweetForm(request.POST)
    if form.is_valid():
        input = request.POST.get('param')
        print(input)
        tweet_to_edit = Tweet.objects.all().get(text=input)
        tweet_to_edit.text = form.cleaned_data['text']
        hashtags = create_hashtags(form)
        tweet_to_edit.hashtag_in_tweet.set(hashtags)
        tweet_to_edit.save()

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
            id_tweet=random.randrange(0, 999999999999),
            text=form.cleaned_data['text'],
            user=user
        )
        hashtags = create_hashtags(form)
        tweet.hashtag_in_tweet.set(hashtags)
        tweet.save()

        impact = Impact.objects.create(
            tweet=tweet,
            stat=Statistics.objects.get(type_stat="RT"),
            stat_value=0
        )
        impact.save()
        impact = Impact.objects.create(
            tweet=tweet,
            stat=Statistics.objects.get(type_stat="FAV"),
            stat_value=0
        )
        impact.save()

def create_tweet_from_API(request):
    input = request.POST.get('param')
    output = user_api.get_tweets(input)

    created = TwitterUser.objects.all().filter(username="@"+output["Username"]).count() != 0
    if not created:
        user = TwitterUser.objects.create(
            username="@"+output["Username"],
            realname=output["Real Name"],
            following=0,
            followers=0,
            profile_picture="img/profilepicture5.jpg",
        )
        user.save()
    else:
        user = TwitterUser.objects.get(username="@"+output["Username"])

    hashtags, text = find_hashtags_from_API(output["Text"])
    tweet = Tweet.objects.create(
        id_tweet=random.randrange(0, 999999999999),
        text=text,
        user=user
    )

    tweet.hashtag_in_tweet.set(hashtags)
    tweet.save()
    impact = Impact.objects.create(
        tweet=tweet,
        stat=Statistics.objects.get(type_stat="RT"),
        stat_value=int(output["RT"])
    )
    impact.save()
    impact = Impact.objects.create(
        tweet=tweet,
        stat=Statistics.objects.get(type_stat="FAV"),
        stat_value=int(output["FAV"])
    )
    impact.save()

def find_hashtags_from_API(hashtags):
    word_array = hashtags.split()
    hashtag = []
    final_text = ""
    for ht in word_array:
        if ht[0] == '#':
            hashtags, created = Hashtag.objects.get_or_create(hashtag=ht)
            hashtag.append(hashtags)
        else:
            final_text += ht
            final_text += " "

    return hashtag, final_text


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

