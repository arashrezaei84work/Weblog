from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
app_name = 'users'

urlpatterns = [

    path('login/',auth_views.LoginView.as_view(),name='login'),       
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),



    path('register/',views.register_view,name='register'),

    # ===================================
    path('author/<int:user_id>',views.author_view,name='author'),
    path('users/profile/',views.profile_view,name='profile'),

    path('users/profile/my_posts',views.my_posts,name='my_posts'),
    path('users/profile/create_post',views.create_post,name='create_post'),
    path('users/profile/edit_post/<int:post_id>',views.edit_post,name='edit_post'),

    path('users/profile/my_comments',views.my_comments,name='my_comments'),

    path('users/profile/my_posts/delete/<int:post_id>',views.delete_post,name='delete')


]
