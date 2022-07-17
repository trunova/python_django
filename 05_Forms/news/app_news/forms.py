import django.forms
from app_news.models import *
from django.forms import ModelForm, Textarea, CharField

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

class NewsCreateForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class CommentFormLogin(ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment_text']