from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm, CreatePostForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment, Category
# Create your views here.

def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.add_message(request,messages.SUCCESS,'registeration is  successful!')
                form.save()
                return redirect('users:login')
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
    if request.method == 'POST' :
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success( request,'اطلاعات کاربری با موفقیت تغییر کرد.')
            return redirect('users:profile')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request,'users/profile.html',{'form':form})

def my_posts(request):
    posts = Post.objects.filter(author__username=request.user.username)
    return render(request,'users/my_posts.html',{'posts':posts})

def edit_post(request):
    post = Post.objects.filter(author__username=request.user.username)
    return render(request,'users/edit_post.html',{'post':post})


def my_comments(request):
    # post = Post.objects.filter(status=1)
    comments = Comment.objects.filter(name=request.user.username,approved=1)
    return render(request,'users/my_comments.html',{'comments':comments})


def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'پست شما با موفقیت ذخیره شد و پس از بررسی مدیران سایت نمایش داده میشود.')
        else:
            messages.add_message(request, messages.ERROR, 'در ثبت پست خطایی رخ داد.')
    category = Category.objects.all()
    form = CreatePostForm()
    return render(request, 'users/create_post.html',{'form':form,'category':category})