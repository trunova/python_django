from django import forms
from django.forms import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, Textarea, CharField, TextInput, Select, NumberInput, PasswordInput

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'teg']
        widgets = {'title': TextInput(attrs={
            'class': 'form__input',
            'placeholder': 'title',
            'required': True
            }),
            'content': Textarea(attrs={
                'class': 'form__input form__news',
                'placeholder': 'content',
                'required': True
            }),
            'teg': TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'teg',
                'required': False
            })
        }


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form__input',
            'placeholder': 'name',
            'required': True
        }
    ))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form__input',
            'placeholder': 'password',
            'required': True
        }
    ))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form__input',
            'placeholder': 'repeat password',
            'required': True
        }
    ))
    tel = forms.CharField(label='Телефон', widget=forms.NumberInput(
        attrs={
            'type': 'tel',
            'class': 'form__input',
            'placeholder': '+7 *** *** ** **',
            'required': False
        }
    ))
    city = forms.CharField(label='Город', widget=forms.TextInput(
        attrs={
            'class': 'form__input',
            'placeholder': 'city',
            'required': False
        }
    ))
    type_user = forms.CharField(label='Тип пользователя', widget=forms.Select(
        choices= (('ordinary', 'Обычный'),
                  ('expectation', 'Верифицированный (для верификация необходимо решение модератора)'),),
        attrs={
            'class': 'form__select',
            'placeholder': 'city',
            'required': False
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'tel', 'city', 'type_user']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form__input',
            'placeholder': 'name',
            'required': True
        }
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form__input',
            'placeholder': 'password',
            'required': True
        }
    ))


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': Textarea(attrs={
                'class': 'form__input form__comment',
                'placeholder': 'Введите текст комментария',
                'required': True
            })
        }

class CommentFormLogin(ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment_text']
        widgets = {'username': TextInput(attrs={
            'type': 'text',
            'class': 'form__input',
            'placeholder': 'Введите имя',
            'required': True
            }),
            'comment_text': Textarea(attrs={
                'class': 'form__input form__comment',
                'placeholder': 'Введите текст комментария',
                'required': True
            })
        }