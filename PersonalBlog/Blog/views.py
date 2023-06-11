from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = list(Post.objects.values())
    return render(request, 'index.html', {'posts': posts})

def newPost(request):
    return render(request, 'newPost.html')