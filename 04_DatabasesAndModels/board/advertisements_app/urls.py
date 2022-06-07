from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path('advertisements/', AdvertisementListView.as_view(), name='advertisements'),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement_detail')
]
