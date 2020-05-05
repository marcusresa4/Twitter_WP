from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.oauth2.urls')),
    path('complete/google-oauth2/twittermonitoring/', include('apps.twitter.urls')),
]
