from django.contrib import admin
from apps.twitter_app.models import User, Tweet, Hashtag, Statistics, Impact, TwitterUser

class UserAdmin(admin.ModelAdmin):
    pass

class TweetAdmin(admin.ModelAdmin):
    pass

class HashtagAdmin(admin.ModelAdmin):
    pass

class StatisticsAdmin(admin.ModelAdmin):
    pass

class ImpactAdmin(admin.ModelAdmin):
    pass

class TwitterUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(Statistics, StatisticsAdmin)
admin.site.register(Impact, ImpactAdmin)
admin.site.register(TwitterUser, TwitterUserAdmin)
