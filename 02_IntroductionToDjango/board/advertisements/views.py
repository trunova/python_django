from django.shortcuts import render
from django.http import HttpResponse

def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_list.html', {})

def python_developer(request, *args, **kwargs):
    return render(request, 'advertisements/python_developer.html', {})

def java_developer(request, *args, **kwargs):
    return render(request, 'advertisements/java_developer.html', {})

def java_developer_pro(request, *args, **kwargs):
    return render(request, 'advertisements/java_developer_pro.html', {})

def web_developer(request, *args, **kwargs):
    return render(request, 'advertisements/web_developer.html', {})

def c_developer(request, *args, **kwargs):
    return render(request, 'advertisements/c_developer.html', {})