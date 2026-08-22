from django.urls import path
from blog.views import blog_view,category_view ,single_view, like_view, search_view
app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='blog'),

    path('search/',search_view,name='search'),

    path('category/<str:cat>',category_view,name='category'),
    path('post/<str:slug>',single_view,name='single'),
    path('post/<str:slug>/<int:pid>',like_view,name='like'),
    
]
