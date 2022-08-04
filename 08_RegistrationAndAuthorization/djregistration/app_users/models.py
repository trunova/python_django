from django.db import models
from django.template.defaultfilters import truncatechars  # or truncatewords
from django.contrib.auth.admin import User
from phonenumber_field.modelfields import PhoneNumberField


class News(models.Model):
    FLAG_CHOICES = [
        (True, 'actively'),
        (False, 'not active')
    ]
    FLAG_PUBLICATION = [
        ('published', 'published'),
        ('not published', 'not published'),
        ('pending publication', 'pending publication')
    ]
    title = models.CharField(verbose_name='Название', max_length=1000)
    content = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    edit_date = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    flag = models.BooleanField(primary_key=False, choices=FLAG_CHOICES, default='n')
    flag_publication = models.CharField(verbose_name='Состояние', blank=True,max_length=300, choices=FLAG_PUBLICATION, default='not published')
    teg = models.CharField(verbose_name='Тег', blank=True, default=None, max_length=100)

    def short_title(self):
        return f'{self.title[:50]} ...'

    def __str__(self):
        return f'{self.title}, {self.create_date}, {self.flag}'

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новость'
        permissions = (('can_publish', 'Может публиковать'),)


class Comment(models.Model):
    username = models.CharField(verbose_name='Имя пользователя', max_length=100)
    comment_text = models.TextField(verbose_name='Комментарий')
    news = models.ForeignKey('News', default=None, null=True,
                             on_delete=models.CASCADE, related_name='ad_news')
    user = models.ForeignKey(User, default=None, null=True,
                             on_delete=models.CASCADE, related_name='ad_user')

    @property
    def short_comment_text(self):
        return truncatechars(self.comment_text, 15)

    def __str__(self):
        return f'{self.username}, {self.short_comment_text}'


class Profile(models.Model):
    FLAG_VERIFICATION = [
        ('ordinary', 'ordinary'),
        ('expectation', 'expectation'),
        ('verified', 'verified')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = PhoneNumberField(verbose_name='Номер телефона', unique=True, null=False, blank=False)
    city = models.CharField(verbose_name='Город', blank=True, max_length=100)
    type_user = models.CharField(verbose_name='Тип пользователя', blank=True, max_length=300, choices=FLAG_VERIFICATION, default='ordinary')
    news_count = models.IntegerField(verbose_name='Количество опубликованных новостей', default=0)