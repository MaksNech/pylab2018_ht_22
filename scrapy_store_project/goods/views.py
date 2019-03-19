
import redis
import json
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
import os


from . import redis_client


class StartScrapingView(View):
    # def __init__(self):
    #     super(StartScrapingView, self).__init__()
    #     self.r = redis.Redis(
    #         host='localhost',
    #         port=6379
    #     )

    def get(self, request, *args, **kwargs):
        return render(self.request, 'goods/scraping.html')

    def post(self, request, *args, **kwargs):
        redis_client.conn.lpush(
            'net_a_porter_bags:start_urls',
            'https://www.net-a-porter.com/us/en/d/Shop/Bags/All?cm_sp=topnav-_-bags-_-topbar&pn=1&npp=\
                                                60&image_view=product&dScroll=0'
        )
        return render(self.request, 'goods/scraping.html')



def index(request):
    # goods = Good.objects.all()
    goods = []
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    p=os.path.join(BASE_DIR, 'store')
    print(p)
    return render(request, 'goods/index.html', context={'goods': goods})



