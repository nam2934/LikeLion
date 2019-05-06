from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(requset):
    blog = Blog()
    blog.title = requset.GET['title']
    blog.body = requset.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/'+str(blog.id))


