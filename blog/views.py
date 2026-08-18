from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Comment
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
@login_required
def blog_view(request,**kwargs):
    if kwargs.get('cat') != None:
        posts = posts.filter(category__name=kwargs['cat'])
    posts = Post.objects.filter(status=1)
    paginator = Paginator(posts,2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {'posts':page_obj}
    return render(request, 'blog/blog.html', context)

@login_required
def single_view(request,slug):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            messages.add_message(request,messages.SUCCESS,'کامنت شما ثبت شد و بعد از تایید توسط ادمین سایت نمایش داده میشود.')
            form.save()
        else:
            messages.add_message(request,messages.ERROR,'کامنت ثبت نشد درخواست خود را دوباره بررسی کنید.')
    post = get_object_or_404(Post, slug=slug)
    post.post_view += 1
    post.save()
    comments = Comment.objects.filter(post_id=post.id,approved=1)
    form = CommentForm()
    context = {
        'post':post,
        'form':form,
        'comments':comments
        }
    return render(request, 'blog/single_blog.html',context)

@login_required
def category_view(request,cat):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat)
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

def like_view(request,pid):
    post = Post.objects.filter(id=pid)


