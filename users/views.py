from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm, CreatePostForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment, Category
from django.contrib.auth.models import User

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
def author_view(request, user_id):
    author = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(status=1, author=author)
    total_views = sum(post.post_view for post in posts)
    context = {
        'posts':posts,
        'author':author,
        'total_views':total_views
    }
    return render(request,'users/author.html',context )


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



def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id,author=request.user)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            categories = request.POST.getlist('category')
            post.category.set(categories)

            messages.success(request,'پست شما با موفقیت ویرایش شد.')
            return redirect('users:my_posts')
    else:
        form = CreatePostForm(instance=post)
    category = Category.objects.all()
    context = {
        'post':post,
        'form':form,
        'category':category
    }
    return render(request,'users/edit_post.html', context)




def my_comments(request):
    # post = Post.objects.filter(status=1)
    comments = Comment.objects.filter(name=request.user.username,approved=1)
    return render(request,'users/my_comments.html',{'comments':comments})


def create_post(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()   # چون از commit=False استفاده کردیم، دسته‌بندی‌ها (m2m) رو دستی ذخیره کن
            messages.add_message(request, messages.SUCCESS,
                'پست شما با موفقیت ذخیره شد و پس از بررسی مدیران سایت نمایش داده می‌شود.')
            form = CreatePostForm()
        else:
            messages.add_message(request, messages.ERROR,
                'در ثبت پست خطایی رخ داد. لطفاً فیلدها را بررسی کنید.')
    else:
        form = CreatePostForm()
    return render(request, 'users/create_post.html', {'form': form, 'category': category})


@login_required
def delete_post(request,post_id=None):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect('users:my_posts')