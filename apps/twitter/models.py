from django.db import models
from django.contrib.auth import models as auth_models


class TwitterUser(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    following = models.PositiveIntegerField()
    followers = models.PositiveIntegerField()
    tweet = models.ManyToManyField('Tweet', related_name= 'personal_tweets')

    def __str__(self):
        return self.username

class Tweet(models.Model):
    id_tweet = models.PositiveIntegerField(primary_key=True, default=123)
    text = models.TextField(max_length=280,default="", help_text="280 characters max")
    hashtag_in_tweet= models.ManyToManyField('Hashtag', related_name='hashtags_tweet')
    def __str__(self):
        return self
    
class Hashtag(models.Model):
    hashtag = models.TextField(primary_key=True, default="", max_length=279) # We have to keep in mind character "#"

    def __str__(self):
        return self

class Statistics(models.Model):
    type_stat = models.CharField(primary_key=True, default="", max_length=7) # Retweet is the longest (likes length 5)    
    def __str__(self):
        return self

class Impact(models.Model):
    id_tweet = models.ForeignKey('Tweet', default=123, on_delete=models.CASCADE)
    type_stat = models.ForeignKey('Statistics',default="", on_delete=models.CASCADE)
    stat_value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self
