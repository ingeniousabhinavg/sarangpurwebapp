from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.

silderData = Slider.objects.all()
placesData = Places.objects.all()
authoritiesData = Authorities.objects.all()
newsData = Latestnews.objects.all().order_by('pub_date')[:5]

context = {
    'slider':silderData,
    'places': placesData,
    'authorities': authoritiesData,
    'news':newsData
}

def index(request):
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', context)

def news(request):
    return render(request, 'news.html', context)