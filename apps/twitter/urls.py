from django.urls import path
from apps.twitter import views

urlpatterns = [
	path('', views.twitter, name='feed'),
	path('user/<username>', views.twitteruser, name='tweets_user'),
	path('hashtag/<hashtag>', views.twitterhashtag, name='tweets_hashtag'),
	path('api/', views.external, name="api")
]