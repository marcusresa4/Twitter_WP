from django.contrib.auth.models import User
from django.test import TestCase

from .models import *


class RestaurantReviewTestCase(TestCase):
    def setUp(self):
        user1 = TwitterUser.objects.create(username="user1", realname="Santi Nolla", following=1, followers=100000)
        user2 = TwitterUser.objects.create(username="user2", realname="Oleguer", following=300, followers=10)
        user3 = TwitterUser.objects.create(username="user3", realname="RDT", following=120, followers=1000000)
        trendy = Tweet.objects.create(name="Nuñista se nace, no se hace", user=user1, id_tweet=123,
                                      hashtag_in_tweet="#Cruyfftraidor")
        not_trendy = Tweet.objects.create(name="Visca el fcb", user=user2, id_tweet=1234,
                                          hashtag_in_tweet="#triplet")
        trendy2 = Tweet.objects.create(name="Que malament juguem", user=user3, id_tweet=12345,
                                       hashtag_in_tweet="#VALVERDEOUT")
        not_trendy2 = Tweet.objects.create(name="Gallego president!", user=user2, id_tweet=12345,
                                           hashtag_in_tweet="#rcde")

    def test_hashtag_works(self):
        """The hashtag for a tweet is properly added"""
        tweet = Tweet.objects.get(name="Gallego president!")
        self.assertEqual(tweet.hashtag_in_tweet, "#rcde")

    def test_text_works(self):
        """The text of a tweet is properly added"""
        tweet = Tweet.objects.get(id_tweet=12345)
        self.assertEqual(tweet.text, "Que malament juguem")

    def test_user_from_tweet(self):
        """The user who has published a tweet is corresponds"""
        tweet = Tweet.objects.get(id_tweet=1234)
        self.assertEqual(tweet.username, "user2")

    def test_id_tweet(self):
        """The id from the tweet properly corresponds"""
        tweet = Tweet.objects.get(text="Nuñista se nace, no se hace")
        self.assertEqual(tweet.id_tweet, 123)
