from multiprocessing import context
from django.views import generic
from django.shortcuts import render
from .models import *
# Create your views here.

silderData = Slider.objects.all()
placesData = Places.objects.all()
authoritiesData = Authorities.objects.all()
newsData = Latestnews.objects.all().order_by('pub_date')[:5]
blogData = Post.objects.filter(status=1).order_by('-created_on')

context = {
    'slider':silderData,
    'places': placesData,
    'authorities': authoritiesData,
    'news':newsData,
    'blog':blogData,
}

def index(request):
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', context)

def news(request):
    return render(request, 'news.html', context)

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'indexx.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'