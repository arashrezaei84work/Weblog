from django import template
from blog.models import Post,Category

register = template.Library()


@register.inclusion_tag('blog/category.html')
def categories():
    post = Post.objects.filter(status=1)
    cats = Category.objects.all()
    cat_dict = {}
    for name in cats:
        cat_dict[name] = post.filter(category=name).count
    return {'cats' : cat_dict}

@register.inclusion_tag('blog/latespost.html')
def latespost(args=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:args]
    return {'posts':posts}


@register.inclusion_tag('blog/favorite_posts.html')
def fav_posts():
    posts = Post.objects.filter(status=1).order_by('likes')[:6]
    return {'posts':posts}
