from django.contrib import admin
from app_users.models import News, Comment, Profile
from django.contrib.auth.models import Group, User


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'flag_publication']
    list_filter = ['teg', 'create_date']
    inlines = [CommentInLine]
    actions = ['mark_as_actively', 'mark_as_not_active', 'mark_as_publication', 'mark_as_not_publication']

    def mark_as_not_active(self, request, queryset):
        queryset.update(flag=False)

    def mark_as_actively(self, request, queryset):
        queryset.update(flag=True)

    def mark_as_not_publication(self, request, queryset):
        queryset.update(flag_publication='not published')

    def mark_as_publication(self, request, queryset):
        queryset.update(flag_publication='published')

    mark_as_publication.short_description = 'Перевести в статус \"опубликовано\"'
    mark_as_not_publication.short_description = 'Перевести в статус \"не опубликовано\"'
    mark_as_actively.short_description = 'Перевести в статус \"активно\"'
    mark_as_not_active.short_description = 'Перевести в статус \"неактивно\"'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'short_comment_text', 'news']
    actions = ['removed_by_admin']

    def removed_by_admin(self, request, queryset):
        queryset.update(comment_text='Удалено администратором')

    removed_by_admin.short_description = 'Проставить текст комментария \"Удалено администратором\"'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'tel', 'type_user']
    actions = ['mark_as_verified']

    def mark_as_verified(self, request, queryset):
        queryset.update(type_user='verified')
        group = Group.objects.get(name='Верифицированные пользователи')
        profiles = Profile.objects.all()
        for profile in profiles:
            if profile.FLAG_VERIFICATION == 'expectation':
                group.user_set.add(profile.user)

    mark_as_verified.short_description = 'Перевести в статус \"верифицированный пользователь\"'
