from behave import *
from django.test import Client
from django.contrib.auth.models import User

use_step_matcher("parse")


@given('Exists a user logged {username} {name} {surname} {password}')
def step_impl(context, username, name, surname, password):
    from django.contrib.auth.models import User
    c = Client()
    user = User.objects.create_user(username=username, first_name=name, last_name=surname,
                                    email='user@example.com', password=password)
    c.force_login(user)


@given('That {username} is logged in')
def step_impl(context, username):
    from django.contrib.auth.models import User
    c = Client()
    user = User.objects.get(username=username)
    c.force_login(user)


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
