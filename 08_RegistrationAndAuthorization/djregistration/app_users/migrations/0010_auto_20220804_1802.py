# Generated by Django 2.2 on 2022-08-04 15:02

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0009_auto_20220803_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=100, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='news',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редактирования'),
        ),
        migrations.AlterField(
            model_name='news',
            name='flag_publication',
            field=models.CharField(blank=True, choices=[('published', 'published'), ('not published', 'not published'), ('pending publication', 'pending publication')], default='not published', max_length=300, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='news_count',
            field=models.IntegerField(default=0, verbose_name='Количество опубликованных новостей'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_user',
            field=models.CharField(blank=True, choices=[('ordinary', 'ordinary'), ('expectation', 'expectation'), ('verified', 'verified')], default='ordinary', max_length=300, verbose_name='Тип пользователя'),
        ),
    ]