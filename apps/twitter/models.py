
from django.db import models
from django.contrib.auth import models as auth_models


class TwitterUser(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    realname = models.CharField(max_length=25)
    following = models.PositiveIntegerField()
    followers = models.PositiveIntegerField()
    numtweets = models.PositiveIntegerField()

    def __str__(self):
        return self.username

class Tweet(models.Model):
    id_tweet = models.PositiveIntegerField(primary_key=True)
    text = models.TextField(max_length=280, help_text="280 characters max")
    hashtag_in_tweet= models.ManyToManyField('Hashtag', related_name='hashtags_tweet')
    user = models.ForeignKey('TwitterUser' , on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Hashtag(models.Model):
    hashtag = models.TextField(primary_key=True, max_length=279) # We have to keep in mind character "#"

    def __str__(self):
        return self.hashtag


class Statistics(models.Model):
    type_stat = models.CharField(primary_key=True, max_length=7) # Retweet is the longest (likes length 5)

    def __str__(self):
        return self.type_stat


class Impact(models.Model):
    id_tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    type_stat = models.ForeignKey('Statistics', on_delete=models.CASCADE)
    stat_value = models.PositiveIntegerField()

    def __str__(self):
        return self