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