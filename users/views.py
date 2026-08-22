from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
# Create your views here.

def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.add_message(request,messages.SUCCESS,'registeration is  successful!')
                form.save()
                return redirect('/accounts/login/')
            else:
                messages.add_message(request,messages.ERROR,'registeration is not successful!')
                return render(request,'registration/register.html',{'form':form})
        else:
            form = RegisterForm()
            return render(request,'registration/register.html',{'form':form})
    else:
        return redirect('/')


@login_required
def author_view(request):
    return render(request,'users/author.html')

@login_required
def profile_view(request):
    return render(request,'users/profile.html')

def my_posts(request):
    posts = Post.objects.filter(author__username=request.user.username)
    return render(request,'users/my_posts.html',{'posts':posts})


def my_comments(request):
    # post = Post.objects.filter(status=1)
    comments = Comment.objects.filter(name=request.user.username,approved=1)
    return render(request,'users/my_comments.html',{'comments':comments})


def create_post(request):
    return render(request, 'users/create_post.html')