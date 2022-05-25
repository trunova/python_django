from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from typing import Callable, Any

def request_counter(func: Callable) -> Any:
    def wrapped_func(*args, **kwargs):
        wrapped_func.counter += 1
        return func(*args, **kwargs)

    wrapped_func.counter = 0
    return wrapped_func


class Advertisements(View):

    @request_counter
    def get(self, request):
        advertisements = [
            'Back-end Developer (Solidity+Django)',
            'Solution-инженер/архитектор',
            'Senior Machine Learning Engineer (Remote)',
            'Разработчик Java'
        ]
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                          'counter': self.get.counter})

    @request_counter
    def post(self):
        return render(request, 'advertisements/advertisement_post.html', {'counter': self.post.counter})


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'ВОРОНЕЖ, ФРИДРИХА ЭНГЕЛЬСА, 11'
        context['phone'] = '+7 (915) 549-59-96'
        context['email'] = 'bigapizza@mail.ru'

        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'New Balance'
        context['descr'] = """ New Balance — американский спортивный бренд, 
        основанный в 1906 году. Это один из самых опытных и крупных производителей спортивного сегмента. 
        Непревзойденный мастер классических кроссовок. Один из немногих брендов, который до сих пор выпускает 
        обувь на фабриках в Англии и США. """
        return context

class MainPage(TemplateView):
    template_name = 'advertisements/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_regions'] = ["Москва",
                             "Ханты-Мансийский автономный округ — Югра",
                             "Московская область",
                             "Санкт-Петербург",
                             "Ямало-Ненецкий автономный округ",
                             "Республика Татарстан",
                             "Краснодарский край",
                             "Красноярский край",
                             "Свердловская область",
                             "Республика Башкортостан",
                             "Самарская область",
                             "Челябинская область",
                             "Ростовская область",
                             "Иркутская область",
                             "Нижегородская область",
                             "Пермский край",
                             "Тюменская область",
                             "Новосибирская область",
                             "Кемеровская область — Кузбасс",
                             "Сахалинская область",
                             "Ленинградская область",
                             "Республика Саха (Якутия)",
                             "Оренбургская область",
                             "Воронежская область",
                             "Белгородская область",
                             "Волгоградская область",
                             "Приморский край",
                             "Ставропольский край",
                             "Саратовская область",
                             "Хабаровский край",
                             "Омская область",
                             "Республика Коми",
                             "Тульская область",
                             "Удмуртская Республика",
                             "Республика Дагестан",
                             "Вологодская область",
                             "Липецкая область",
                             "Томская область",
                             "Ярославская область",
                             "Астраханская область",
                             "Алтайский край",
                             "Архангельская область",
                             "Мурманская область",
                             "Калужская область",
                             "Калининградская область",
                             "Тверская область",
                             "Владимирская область",
                             "Курская область",
                             "Пензенская область",
                             "Республика Крым",
                             "Рязанская область",
                             "Ульяновская область",
                             "Кировская область",
                             "Тамбовская область",
                             "Брянская область",
                             "Забайкальский край",
                             "Смоленская область",
                             "Ненецкий автономный округ",
                             "Амурская область",
                             "Чувашская Республика",
                             "Республика Карелия",
                             "Новгородская область",
                             "Камчатский край",
                             "Республика Хакасия",
                             "Орловская область",
                             "Республика Мордовия",
                             "Республика Бурятия",
                             "Курганская область",
                             "Ивановская область",
                             "Чеченская Республика",
                             "Костромская область",
                             "Республика Марий Эл",
                             "Магаданская область",
                             "Псковская область",
                             "Кабардино-Балкарская Республика",
                             "Республика Северная Осетия",
                             "Республика Адыгея",
                             "Севастополь",
                             "Чукотский автономный округ",
                             "Карачаево-Черкесская Республика",
                             "Республика Калмыкия",
                             "Республика Тыва Еврейская автономная область, Республика Ингушетия",
                             "Республика Алтай"]
        return context