from behave import *
from django.test import Client
import time

use_step_matcher("parse")


@given('Exists a user logged {username} {name} {surname} {password}')
def step_impl(context, username, name, surname, password):
    from django.contrib.auth.models import User
    user = User.objects.create_superuser(username='user', email='xicagoneverminds@gmail.com', password='user')


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/admin'))
    time.sleep(0.2)
    context.browser.find_by_xpath('//*[@id="id_username"]').fill('user')
    time.sleep(0.2)
    context.browser.find_by_xpath('//*[@id="id_password"]').fill('user')
    time.sleep(0.2)
    context.browser.find_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    context.browser.find_by_xpath('//*[@id="user-tools"]/a[1]').click()
    context.browser.find_by_xpath('/html/body/div/a[1]').click()


@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('logout'))
    assert context.browser.is_text_present('login')


@then('Server responds with page containing "{message}"')
def step_impl(context, message):
    assert context.browser.is_text_present(message)


@then('There is "{link_text}" link available')
def step_impl(context, link_text):
    assert context.browser.is_element_present_by_xpath('//a[text()="' + link_text + '"]')


@then('There is no "{link_text}" link available')
def step_impl(context, link_text):
    assert context.browser.is_element_not_present_by_xpath('//a[text()="' + link_text + '"]')


@then("I'm redirected to the login form")
def step_impl(context):
    assert context.browser.url.startswith(context.get_url('social'))