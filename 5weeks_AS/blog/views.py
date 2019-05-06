from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blog
from .models import Comment
from django.core.paginator import Paginator
from .forms import CommentForm
# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'blogs':blogs, 'posts':posts})

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

def create_comment(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('detail',post.pk)
    else:
        form = CommentForm(request.POST)
        return render(request, 'blog/comment.html', {'form':form})