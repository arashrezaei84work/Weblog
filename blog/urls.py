from django.urls import path
from blog.views import blog_view,category_view ,single_view
app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='blog'),
    path('category/<str:cat>',category_view,name='category'),
    path('post/<str:slug>',single_view,name='single'),
    
]
