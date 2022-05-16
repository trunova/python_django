from django.urls import path
from .import views

urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path('python_developer/', views.python_developer, name='python_developer'),
    path('java_developer/', views.java_developer, name='java_developer'),
    path('java_developer_pro/', views.java_developer_pro, name='java_developer_pro'),
    path('web_developer/', views.web_developer, name='web_developer'),
    path('c_developer/', views.c_developer, name='c_developer'),
]