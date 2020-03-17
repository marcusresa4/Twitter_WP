from django.urls import path
from apps.twitter import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
]