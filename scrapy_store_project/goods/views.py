from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #goods = Good.objects.all()
    goods=[]

    return render(request, 'goods/index.html', context={'goods': goods})
