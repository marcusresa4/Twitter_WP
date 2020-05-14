from behave import *
from django.test import Client

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
