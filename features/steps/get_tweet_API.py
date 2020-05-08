from behave import *
import operator
from django.db.models import Q
import time

from splinter.exceptions import ElementDoesNotExist
use_step_matcher("parse")



@when('I get a Tweet from API')
def step_impl(context):
    from apps.twitter.models import Statistics
    x = Statistics.objects.create(type_stat="RT")
    x.save()
    x = Statistics.objects.create(type_stat="FAV")
    x.save()
    i=1
    for row in context.table:
        try:
            context.browser.find_by_xpath('/html/body/div['+str(i)+']/div[2]/div[1]/h2/button').click()
            time.sleep(2)
            context.browser.find_by_xpath('/html/body/div['+str(i)+']/div[2]/div[2]/div/form/label/input').fill(row[0])
            time.sleep(2)
            context.browser.find_by_xpath('/html/body/div['+str(i)+']/div[2]/div[2]/div/form/button').click()
            time.sleep(0.2)
        except ElementDoesNotExist:
            pass
        i+=1