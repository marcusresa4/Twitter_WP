from django.urls import path
from apps.twitter import views

# hello_world App URL Configuration
# This file contains a list of URL patterns that correspond to various views functions.

urlpatterns = [
	path('', views.twitter, name='feed'),
	path('user/<username>', views.twitteruser, name='tweets_user'),
	path('hashtag/<hashtag>', views.twitterhashtag, name='tweets_hashtag')
]