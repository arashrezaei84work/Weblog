from django.urls import path
from accounts import views
app_name = 'accounts'

urlpatterns = [
    path('author/',views.author_view,name='author'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.register_view,name='register'),
    path('login/profile/',views.profile_view,name='profile'),

    path('login/profile/my_posts',views.my_posts,name='my_posts'),
    path('login/profile/create_post',views.create_post,name='create_post'),

    path('login/profile/my_comments',views.my_comments,name='my_comments'),

    path('logout/',views.logout_view,name='logout'),
]
