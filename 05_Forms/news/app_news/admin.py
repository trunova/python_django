from django.contrib import admin
from app_news.models import News, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass