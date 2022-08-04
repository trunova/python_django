import datetime
from django.shortcuts import render
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from app_users.models import News, Comment, Profile
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group


class ListNews(View):
    def get(self, request: WSGIRequest):
        news = []
        group = Group.objects.all()
        for n in News.objects.order_by('create_date'):
            if n.flag_publication == 'published':
                news.append(n)
        context = {}
        if request.user.groups.filter(name='Обычные пользователи').exists():
            context['group'] = 'Обычные'
        context['news_list_first'] = news[:len(news):2]
        context['news_list_second'] = news[1:len(news):2]
        return render(request, 'app_users/news.html', context)


    def post(self, request: WSGIRequest):
        news = News.objects.all()
        context = {}
        context['news'] = news

        if request.POST.get('news__create'):
            return HttpResponseRedirect("/app_users/create/")
        return render(request, 'app_users/news.html', context)


class NewsCreate(View):
    def get(self, request: WSGIRequest):
        form = NewsForm()
        context = {}
        context['form'] = form
        return render(request, 'app_users/news_creation.html', context)

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
                    flag=False,
                    teg=form.cleaned_data.get('teg'),
                    flag_publication='pending publication'
                )
                f.save()
                f.flag = False
                if request.user.is_authenticated:
                    p = request.user.profile
                    p.news_count += 1
                    p.save()
                return HttpResponseRedirect("/app_users/")
        context['news'] = news
        context['form'] = form
        return render(request, 'app_users/news_creation.html', context)


class Registration(View):
    def get(self, request: WSGIRequest):
        form = RegistrationForm()
        context = {}
        context['form'] = form
        return render(request, 'app_users/registration.html', context)

    def post(self, request: WSGIRequest):
        form = RegistrationForm(request.POST)
        context = {}
        if form.is_valid():
            user = form.save()
            profile = Profile(
                user=user,
                tel=form.cleaned_data.get('tel'),
                city=form.cleaned_data.get('city'),
                type_user=form.cleaned_data.get('type_user'),
                news_count=0
            )
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            if form.cleaned_data.get('type_user') == 'ordinary':
                group = Group.objects.get(name='Обычные пользователи')
                group.user_set.add(user)

            return HttpResponseRedirect("/app_users/")
        else:
            context['errors'] = form.errors
            form = RegistrationForm()
            user = None
        context['form'] = form
        context['user'] = user
        return render(request, 'app_users/registration.html', context)



class UserPage(View):
    def get(self, request: WSGIRequest):
        context = {}
        context['user'] = request.user
        return render(request, 'app_users/user_page.html', context)


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
        else:
            form = CommentFormLogin(instance=news)
        context = {}
        context['select_news'] = news
        context['select_comment'] = select_comment
        context['form'] = form
        context['news_id'] = news_id
        return render(request, 'app_users/detail_page.html', context)

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
        if form.is_valid():
            f = Comment(
                username=name,
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
        return render(request, 'app_users/detail_page.html', context)


class Login(LoginView):
    template_name = 'app_users/input.html'
    form_class = LoginForm


class Logout(LogoutView):
    next_page = "../../app_users/"