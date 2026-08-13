from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
# Create your views here.

def blog_view(request,**kwargs):
    if kwargs.get('cat') != None:
        posts = posts.filter(category__name=kwargs['cat'])
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog.html', context)

def single_view(request,slug):
    post = get_object_or_404(Post, slug=slug)
    post.post_view += 1
    post.save()
    context = {'post':post}
    return render(request, 'blog/single_blog.html',context)


def category_view(request,cat):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat)
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

