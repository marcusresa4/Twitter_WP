from django.shortcuts import render
from apps.twitter.models import Tweet, TwitterUser, Statistics, Impact, Hashtag, Rating
from . import user_api
from apps.twitter.forms import TweetForm, EditTweetForm
import random


def twitter(request):
    if request.method == 'POST':
        if "Create Tweet" in request.POST:
            create_tweet(request)
        elif "API" in request.POST:
            create_tweet_from_API(request)
        elif "Edit Tweet" in request.POST:
            edit_tweet(request)
        elif "Delete Tweet" in request.POST:
            delete_tweet(request)
        for i in range(5+1):
            if "Rate"+str(i) in request.POST:
                edit_rating(request, i, "Rate"+str(i))

    tweets = Tweet.objects.all()
    impacts = Impact.objects.all()
    form = TweetForm()
    form_edit = EditTweetForm()
    rating = Rating.objects.all()

    context = { 'tweets'    : tweets,
                'impacts'   : impacts,
                'form'      : form,
                'editform'  : form_edit,
                'rating'    : rating
    }

    return render(request, 'feed.html', context)

def edit_rating(request, rate, name):
    id_tweet = request.POST.get(name)
    rating_to_edit = Rating.objects.all().get(tweet_id=id_tweet)
    rating_to_edit.rate = rate
    rating_to_edit.save()

def delete_tweet(request):
    input = request.POST.get('param')
    if input != None:
        print(input)
        Tweet.objects.all().filter(text=input).delete()

def edit_tweet(request):
    form = EditTweetForm(request.POST)
    if form.is_valid():
        input = request.POST.get('param')
        print(input)
        tweet_to_edit = Tweet.objects.all().get(text=input)
        tweet_to_edit.text = form.cleaned_data['edit_text']
        hashtags = create_hashtags_edit(form)
        tweet_to_edit.hashtag_in_tweet.set(hashtags)
        tweet_to_edit.save()

def create_tweet(request):
    form = TweetForm(request.POST)
    if form.is_valid():
        created = TwitterUser.objects.all().filter(username="@superuser").count() != 0
        number = str(random.random()%5 + 1)
        if not created:
            user = TwitterUser.objects.create(
                username="@superuser",
                realname="User Super",
                following=0,
                followers=0,
                profile_picture="img/profilepicture"+number+".jpg",
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

        rating = Rating.objects.create(
            rate=0,
            tweet=tweet
        )
        rating.save()

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
    if input != None:
        try:
            output = user_api.get_tweets(input)
        except:
            return
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
            text=text[:len(text)-1],
            user=user
        )

        tweet.hashtag_in_tweet.set(hashtags)
        tweet.save()
        rating = Rating.objects.create(
            rate=0,
            tweet=tweet
        )
        rating.save()

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

def create_hashtags_edit(form):
    hashtag = []
    hashtags_str = form.cleaned_data['edit_hashtag_in_tweet'].split()
    for ht in hashtags_str:
        hashtags, created = Hashtag.objects.get_or_create(hashtag=ht)
        hashtag.append(hashtags)

    return hashtag

def twitteruser(request, username):
    tweets = Tweet.objects.filter(
        user__username__contains=username)

    user = TwitterUser.objects.filter(
        username__contains=username
    )
    impacts = Impact.objects.all()
    ratings = Rating.objects.all()
    context = {
        'users': user,
        'tweets': tweets,
        'impacts' : impacts,
        'rating' : ratings
    }

    return render(request, 'tweets_user.html', context)


def twitterhashtag(request, hashtag):
    tweets = Tweet.objects.filter(
        hashtag_in_tweet__hashtag__contains=hashtag)

    impacts = Impact.objects.all()
    ratings = Rating.objects.all()

    context = {
        'hashtag': hashtag,
        'tweets': tweets,
        'impacts' : impacts,
        'rating' : ratings
    }

    return render(request, 'tweets_hashtag.html', context)

