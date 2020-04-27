from behave import *
from django.test import Client
from django.contrib.auth.models import User

use_step_matcher("parse")

#No se si es pot fer ja que s'ha d'introduir un CAPTCHA
@given('I login as user with Google {username} {name} {surname} {password}')
def step_impl(context, username, name, surname, password):
    c = Client()
    user = User.objects.create_user(username=username, first_name=name, last_name=surname,
                                    email='user@example.com', password=password)
    c.force_login(user)

@given('Exists a user logged {username} {name} {surname} {password}')
def step_impl(context, username, name, surname, password):
    User.objects.create_user(username=username, first_name=name, last_name=surname,
                             email='user@example.com', password=password)