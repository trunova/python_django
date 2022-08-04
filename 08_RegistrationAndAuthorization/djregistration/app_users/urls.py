from django.urls import path
from .import views

urlpatterns = [
    path('', views.ListNews.as_view(), name='news'),
    path('<int:news_id>/detailed/', views.NewsDetailed.as_view(), name='detailed'),
    path('create/', views.NewsCreate.as_view(), name='create'),
    path('registration/', views.Registration.as_view(), name='create'),
    path('login/', views.Login.as_view(), name='login'),
    path('user_page/', views.UserPage.as_view(), name='user_page'),
    path('logout/', views.Logout.as_view(), name='logout')
]