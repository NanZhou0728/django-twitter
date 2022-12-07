from django.contrib import admin
from tweets.models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    # 筛选机制
    date_hierarchy = 'created_at'
    list_display = (
        'created_at',
        'user',
        'content',
    )
