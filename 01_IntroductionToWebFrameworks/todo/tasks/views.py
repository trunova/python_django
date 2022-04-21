from django.http import HttpResponse

from django.views import View
import random


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        todo_list = ['<li>Установить python</li>', '<li>Установить django</li>', '<li>Запустить сервер</li>',
                     '<li>Изменить код</li>', '<li>Порадоваться результату</li>']
        random.shuffle(todo_list)
        return HttpResponse('<ul> {list} <ul>'.format(list=''.join(todo_list)))