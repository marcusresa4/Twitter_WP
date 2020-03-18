from django.urls import path
from apps.twitter import views

# hello_world App URL Configuration
# This file contains a list of URL patterns that correspond to various views functions.

urlpatterns = [
	path('', views.twitter, name='feed')
]