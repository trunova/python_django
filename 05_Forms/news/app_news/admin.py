from django.contrib import admin
from app_news.models import News, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'edit_date', 'flag']
    list_filter = ['flag']
    inlines = [CommentInLine]
    actions = ['mark_as_actively', 'mark_as_not_active']

    def mark_as_not_active(self, request, queryset):
        queryset.update(flag=False)

    def mark_as_actively(self, request, queryset):
        queryset.update(flag=True)

    mark_as_actively.short_description = 'Перевести в статус \"активно\"'
    mark_as_not_active.short_description = 'Перевести в статус \"неактивно\"'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'short_comment_text', 'news']
    list_filter = ['username']
    actions = ['removed_by_admin']

    def removed_by_admin(self, request, queryset):
        queryset.update(comment_text='Удалено администратором')

    removed_by_admin.short_description = 'Проставить текст комментария \"Удалено администратором\"'
