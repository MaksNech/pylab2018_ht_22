from django.urls import path
from . import views
from .views import StartScrapingView


urlpatterns = [
    path('', views.index, name='index'),
    path('scraping/', StartScrapingView.as_view(), name='scraping'),


]