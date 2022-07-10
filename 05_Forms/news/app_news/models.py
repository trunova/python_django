from django.db import models

class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    flag = models.BooleanField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    username = models.CharField(verbose_name='Username', max_length=100)
    comment_text = models.TextField(verbose_name='Комментарий')
    news = models.ForeignKey('News', default=None, null=True,
                               on_delete=models.CASCADE, related_name='ad_news')