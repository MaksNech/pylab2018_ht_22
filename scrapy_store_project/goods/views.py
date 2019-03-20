from django.views import View
from django.shortcuts import render
from django.views.generic import ListView

from .models import Bag
from . import redis_client


class StartScrapingView(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'goods/scraping.html')

    def post(self, request, *args, **kwargs):
        redis_client.conn.lpush(
            'net_a_porter_bags:start_urls',
            'https://www.net-a-porter.com/us/en/d/Shop/Bags/All?cm_sp=topnav-_-bags-_-topbar&pn=1&npp=\
                                                60&image_view=product&dScroll=0'
        )
        return render(self.request, 'goods/scraping.html')


class BagListView(ListView):
    model = Bag
    template_name = 'goods/bag_list.html'
    context_object_name = 'bags'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queryset'] = Bag.objects.all()
        return context
