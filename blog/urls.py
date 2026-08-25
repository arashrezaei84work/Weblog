from django.urls import path
from blog.views import blog_view,category_view ,single_view, like_post, search_view, like_comment
app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='blog'),

    path('search/',search_view,name='search'),

    path('category/<str:cat>',category_view,name='category'),
    path('post/<str:slug>',single_view,name='single'),
    path('post/<int:pid>/like',like_post,name='like_post'),
    path('comment/<int:cid>/like',like_comment,name='like_comment'),
    
]
