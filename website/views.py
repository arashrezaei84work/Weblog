from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
# Create your views here.

def home(request):
    post = Post.objects.filter(status=1)
    return render(request, 'website/home.html',{'posts':post})

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')