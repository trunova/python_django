from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()
    price = models.IntegerField(verbose_name='цена', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)

    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True, on_delete=models.CASCADE,
                               related_name='author')
    section = models.ForeignKey('AdvertisementSection', default=None, null=True, on_delete=models.CASCADE,
                               related_name='author')
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=1500)
    email = models.CharField(max_length=1500)
    phone = models.CharField(max_length=12)

class AdvertisementSection(models.Model):
    name = models.CharField(max_length=1500)
