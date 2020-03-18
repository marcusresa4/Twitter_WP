from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.contrib.auth import models as auth_models


class TwitterUser(models.Model):
    username=models.CharField(max_length=15)
    following=models.PositiveIntegerField()
    followers=models.PositiveIntegerField()

    def __str__(self):
        return self.username

class Tweet(models.Model):

    def __str__(self):
        return self
    
class Hashtag(models.Model):

    def __str__(self):
        return self

class Statistics(models.Model):

    def __str__(self):
        return self

class Impact(models.Model):

    def __str__(self):
        return self



