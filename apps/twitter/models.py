from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.contrib.auth import models as auth_models

class User(auth_models.AbstractUser):
    is_active=models.Boolean(default=False) #faltaria parametre name="User activated"

    def __str__(self):
        return self.name

class TwitterUser(models.Model):
    username=models.CharField(max_length=15)
    following=models.PositiveIntegerField()
    followers=models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Tweet(models.Model):

    def __str__(self):
        return self.name
    
class Hashtag(models.Model):

    def __str__(self):
        return self.name

class Statistics(models.Model):

    def __str__(self):
        return self.name

class Impact(models.Model):

    def __str__(self):
        return self.name



