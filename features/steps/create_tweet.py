from functools import reduce

from behave import *
import operator
from django.db.models import Q
import time

from splinter.exceptions import ElementDoesNotExist
use_step_matcher("parse")


@when('I create a Tweet')
def step_impl(context):
    from apps.twitter.models import Statistics
    x = Statistics.objects.create(type_stat="RT")
    x.save()
    x = Statistics.objects.create(type_stat="FAV")
    x.save()
    for row in context.table:
        try:
            context.browser.find_by_xpath('//*[@id="headingOne"]/h2/button').click()
            time.sleep(1)
            context.browser.find_by_xpath('//*[@id="id_text"]').fill(context.table[0][0])
            time.sleep(1)
            context.browser.find_by_xpath('//*[@id="id_hashtag_in_tweet"]').fill(context.table[0][1])
            time.sleep(1)
            context.browser.find_by_xpath('//*[@id="collapseOne"]/div/form/input[2]').click()
        except ElementDoesNotExist:
            pass


@then('I\'m viewing {num:n} tweet created by {user}')
def step_impl(context, user, num):
    from apps.twitter.models import Tweet
    assert len(Tweet.objects.filter(text=context.table[0][0])) == num


@then('There are {count:n} Tweet\'s')
def step_impl(context, count):
    from apps.twitter.models import Tweet
    assert count == Tweet.objects.count()
