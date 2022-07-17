import datetime
from django.shortcuts import render
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from app_news.models import News, Comment
from .forms import NewsForm, NewsCreateForm, CommentForm, CommentFormLogin
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView


class ListNews(View):
    def get(self, request: WSGIRequest):
        news = News.objects.order_by('create_date')
        form = NewsForm()
        context = {}
        context['news'] = news
        context['form'] = form
        return render(request, 'app_news/news_list.html', context)

    def post(self, request: WSGIRequest):
        news = News.objects.all()
        form = NewsForm()
        context = {}
        context['news'] = news
        context['form'] = form
        for i in news:
            id = i.id
            if request.POST.get('edit_news_btn{id}'.format(id=id)):
                return HttpResponseRedirect("/app_news/{news_id}/edit/".format(news_id=id))
            elif request.POST.get('add_com_btn{id}'.format(id=id)):
                return HttpResponseRedirect("/app_news/{news_id}/detailed/".format(news_id=id))

        if request.POST.get('create_news_btn'):
            return HttpResponseRedirect("/app_news/create/")
        return render(request, 'app_news/news_list.html', context)


class NewsEdit(View):
    def get(self, request: WSGIRequest, news_id):
        news = News.objects.get(id=news_id)
        news.flag = True
        form = NewsForm(instance=news)
        context = {}
        context['news'] = news
        context['form'] = form
        context['news_id'] = news_id
        return render(request, 'app_news/news_editing.html', context)

    def post(self, request: WSGIRequest, news_id):
        news = News.objects.get(id=news_id)
        form = NewsForm(request.POST, instance=news)
        context = {}
        if request.POST.get('btn_back'):
            return HttpResponseRedirect("/app_news/")
        elif request.POST.get('save_news'):
            if form.is_valid():
                news.edit_date = datetime.datetime.now()
                news.save()
                return HttpResponseRedirect("/app_news/")

        context['news'] = news
        context['form'] = form
        context['news_id'] = news_id
        return render(request, 'app_news/news_editing.html', context)


class NewsCreate(View):
    def get(self, request: WSGIRequest):
        form = NewsForm()
        context = {}
        context['form'] = form
        return render(request, 'app_news/news_creation.html', context)

    def post(self, request: WSGIRequest):
        news = News.objects.all()
        form = NewsForm(request.POST)
        context = {}
        if request.POST.get('btn_back'):
            return HttpResponseRedirect("/app_news/")
        elif request.POST.get('save_news'):
            if form.is_valid():
                f = News(
                    title=form.cleaned_data.get('title'),
                    content=form.cleaned_data.get('content'),
                    flag=False)
                f.save()
                news.flag = False
                return HttpResponseRedirect("/app_news/")
        context['news'] = news
        context['form'] = form
        return render(request, 'app_news/news_creation.html', context)


class NewsDetailed(View):
    def get(self, request: WSGIRequest, news_id):
        news = News.objects.get(id=news_id)
        news.flag = True
        comments = Comment.objects.all()
        select_comment = []
        for comment in comments:
            if comment.news.id == news_id:
                select_comment.append(comment)
        if request.user.is_authenticated:
            form = CommentForm(instance=news)
        else: form = CommentFormLogin(instance=news)
        context = {}
        context['select_news'] = news
        context['select_comment'] = select_comment
        context['form'] = form
        context['news_id'] = news_id
        return render(request, 'app_news/detailed_news_page.html', context)

    def post(self, request: WSGIRequest, news_id):
        news = News.objects.get(id=news_id)

        select_comment = []

        if request.user.is_authenticated:
            form = CommentForm(request.POST, instance=news)
            name = request.user.username
            user = request.user
        else:
            form = CommentFormLogin(request.POST, instance=news)
            if form.is_valid():
                name = form.cleaned_data.get('username')
            user = None
        context = {}
        if not form.is_valid() and request.POST.get('btn_back'):
            return HttpResponseRedirect("/app_news/")
        elif request.POST.get('save_com'):
            if form.is_valid():
                f = Comment(
                    username=name ,
                    comment_text=form.cleaned_data.get('comment_text'),
                    news=news,
                    user=user)
                f.save()
        comments = Comment.objects.all()
        for comment in comments:
            if comment.news.id == news_id:
                select_comment.append(comment)
        news.flag = False
        context['select_news'] = news
        context['select_comment'] = select_comment
        context['comments'] = comments
        context['form'] = form
        context['news_id'] = news_id
        return render(request, 'app_news/detailed_news_page.html', context)


class Login(LoginView):
    template_name = 'app_news/login.html'

class Logout(LogoutView):
    template_name = 'app_news/logout.html'