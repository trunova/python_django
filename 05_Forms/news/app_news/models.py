from django.db import models
from django.template.defaultfilters import truncatechars  # or truncatewords

class News(models.Model):
    FLAG_CHOICES = [
        (True, 'actively'),
        (False, 'not active')
    ]
    title = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(primary_key=False, choices=FLAG_CHOICES, default='n')

    def __str__(self):
        return f'{self.title}, {self.create_date}, {self.flag}'

class Comment(models.Model):
    username = models.CharField(verbose_name='Username', max_length=100)
    comment_text = models.TextField(verbose_name='Комментарий')
    news = models.ForeignKey('News', default=None, null=True,
                               on_delete=models.CASCADE, related_name='ad_news')

    @property
    def short_comment_text(self):
        return truncatechars(self.comment_text, 15)

    def __str__(self):
        return f'{self.username}, {self.short_comment_text}'
