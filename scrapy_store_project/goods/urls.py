from django.urls import path
from . import views
from .views import StartScrapingView, BagListView

urlpatterns = [
    path('scraping/', StartScrapingView.as_view(), name='scraping'),
    path('', BagListView.as_view(), name='index'),
]
