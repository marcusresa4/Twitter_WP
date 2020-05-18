from behave import *
import operator
from django.db.models import Q
import time

from splinter.exceptions import ElementDoesNotExist
use_step_matcher("parse")

@when('I create a Tweet and Rate It with {count:n} stars')
def step_impl(context, count):
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
            time.sleep(1)
        except ElementDoesNotExist:
            return

    context.browser.find_by_xpath('/html/body/span/div/div/div/form/div/button').click()
    time.sleep(1)
    context.browser.find_by_xpath('/html/body/span/div/div/div/form/div/div/button[3]').click()
    time.sleep(1)


@then('I\'m viewing a tweet with {num_stars:n} stars')
def step_impl(context, num_stars):
    from apps.twitter.models import Rating
    print([x.rate for x in Rating.objects.all()])
    assert len(Rating.objects.filter(rate=num_stars)) == 1