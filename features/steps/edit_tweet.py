from functools import reduce

from behave import *
import operator
from django.db.models import Q
import time

from splinter.exceptions import ElementDoesNotExist
use_step_matcher("parse")

@when('I create and edit a Tweet')
def step_impl(context):
    from apps.twitter.models import Statistics
    x = Statistics.objects.create(type_stat="RT")
    x.save()
    x = Statistics.objects.create(type_stat="FAV")
    x.save()
    i = 1
    for row in context.table:
        if i % 2 == 1:
            try:
                context.browser.find_by_xpath('//*[@id="headingOne"]/h2/button').click()
                time.sleep(0.2)
                context.browser.find_by_xpath('//*[@id="id_text"]').fill(row[0])
                time.sleep(0.2)
                context.browser.find_by_xpath('//*[@id="id_hashtag_in_tweet"]').fill(row[1])
                time.sleep(0.2)
                context.browser.find_by_xpath('//*[@id="collapseOne"]/div/form/input[2]').click()
                #Tweet Created
                i+=1
            except:
                return

        elif i % 2 == 0:
            context.browser.find_by_xpath('//*[@id="headingThreeEdit"]/h2/button').click()
            time.sleep(0.2)
            context.browser.find_by_xpath('//*[@id="id_edit_text"]').fill(row[0])
            time.sleep(0.2)
            context.browser.find_by_xpath('//*[@id="id_edit_hashtag_in_tweet"]').fill(row[1])
            time.sleep(0.2)
            context.browser.find_by_xpath('//*[@id="collapseThree"]/form/button').click()
            i+=1
            #Tweet Edited

@when('I edit the tweet')
def step_impl(context):
    try:
        context.browser.find_by_xpath('//*[@id="headingThreeEdit"]/h2/button').click()
        time.sleep(0.2)
        context.browser.find_by_xpath('//*[@id="id_edit_text"]').fill(context.table[1][0])
        time.sleep(0.2)
        context.browser.find_by_xpath('//*[@id="id_edit_hashtag_in_tweet"]').fill(context.table[1][1])
        time.sleep(0.2)
        context.browser.find_by_xpath('//*[@id="collapseThree"]/form/button').click()
    except ElementDoesNotExist:
        pass
