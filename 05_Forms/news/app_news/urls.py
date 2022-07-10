from django.urls import path
from .import views

urlpatterns = [
    path('', views.ListNews.as_view(), name='news'),
    path('<int:news_id>/edit/', views.NewsEdit.as_view(), name='edit'),
    path('<int:news_id>/detailed/', views.NewsDetailed.as_view(), name='detailed'),
    path('create/', views.NewsCreate.as_view(), name='create')
]
