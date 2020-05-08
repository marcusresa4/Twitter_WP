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
            time.sleep(0.2)
            context.browser.find_by_xpath('//*[@id="id_text"]').fill(row[0])
            time.sleep(0.2)
            context.browser.find_by_xpath('//*[@id="id_hashtag_in_tweet"]').fill(row[1])
            time.sleep(0.2)
            context.browser.find_by_xpath('//*[@id="collapseOne"]/div/form/input[2]').click()
            time.sleep(0.2)
        except ElementDoesNotExist:
            pass


@then('I\'m viewing {num:n} tweet created by {user}')
def step_impl(context, user, num):
    ok=0
    from apps.twitter.models import Tweet
    print([x.text for x in Tweet.objects.all()])
    for row in context.table:
        if(len(Tweet.objects.filter(text=row[0])) == 1):
            ok+=1
    assert ok == num


@then('There are {count:n} Tweet\'s')
def step_impl(context, count):
    from apps.twitter.models import Tweet
    assert count == Tweet.objects.count()