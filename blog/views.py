from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post 
from django.views.generic import TemplateView

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 90) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request,  post):
    post = get_object_or_404(Post, slug=post,
                                   status='published')
    if  post.tipo=='article':
        my_template = 'blog/baseblog.html'
        Sal='blog/post/detail.html'
    else:
        my_template= 'blog/basemap.html'
        Sal='blog/post/map.html'
    return render(request,
                  Sal,
                  {'post': post,'my_template':my_template})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 90
    template_name = 'blog/post/list.html'
    
class AboutPageView(TemplateView):
    template_name = 'blog/post/about.html'

def HomePageView(request):
    posts = Post.objects.filter(tipo="article")[:3]
    maps = Post.objects.filter(tipo="map")[:3]
    return render(request, 'blog/post/home.html', {'posts': posts,'maps': maps})    
