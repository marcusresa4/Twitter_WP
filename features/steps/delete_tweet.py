from functools import reduce

from behave import *
import operator
from django.db.models import Q
import time

from splinter.exceptions import ElementDoesNotExist
use_step_matcher("parse")

@given('I create a Tweet')
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
            context.browser.find_by_xpath('//*[@id="id_text"]').fill(row[0])
            time.sleep(1)
            context.browser.find_by_xpath('//*[@id="id_hashtag_in_tweet"]').fill(row[1])
            time.sleep(1)
            context.browser.find_by_xpath('//*[@id="collapseOne"]/div/form/input[2]').click()
            time.sleep(1)
        except ElementDoesNotExist:
            pass

@when('I delete a Tweet(There are {count:n} tweets)')
def step_impl(context,count):
    try:
        num=count+3
        context.browser.find_by_xpath('/html/body/div['+str(num)+']/form/input[2]').click()
        
    except ElementDoesNotExist:
        pass