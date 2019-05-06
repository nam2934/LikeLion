from django.shortcuts import render

from .models import Blog
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')