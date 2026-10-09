from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category, Comment
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator

from django.db.models import Q


# Create your views here.

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat') != None:
        posts = posts.filter(category__name=kwargs['cat'])
    paginator = Paginator(posts,2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {'posts':page_obj}
    return render(request, 'blog/blog.html', context)




def single_view(request,slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            messages.add_message(request,messages.SUCCESS,'کامنت شما ثبت شد و بعد از تایید توسط ادمین سایت نمایش داده میشود.')
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            messages.add_message(request,messages.ERROR,'کامنت ثبت نشد درخواست خود را دوباره بررسی کنید.')
    post.post_view += 1
    post.save()
    comments = Comment.objects.filter(post=post.id,approved=1)
    form = CommentForm()
    context = {
        'post':post,
        'form':form,
        'comments':comments
        }
    return render(request, 'blog/single_blog.html',context)





def category_view(request,cat):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat)

    paginator = Paginator(posts,2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context = {'posts':page_obj}
    return render(request,'blog/blog.html',context)





def search_view(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(Q(content__icontains=s) | Q(title__icontains=s))
    context = {
        'posts' : posts
    }
    return render(request,'blog/blog.html',context)





@login_required
def like_post(request,pid):
    post = get_object_or_404(Post, id=pid)
    if request.method == 'POST':

        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return redirect('blog:single', slug=post.slug)




@login_required
def like_comment(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    if request.method == 'POST':

        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
    return redirect('blog:single', slug=comment.post.slug)
    
