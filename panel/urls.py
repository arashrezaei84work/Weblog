from django.urls import path
from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('posts/', views.post_list, name='posts'),
    path('posts/<int:post>/toggle/', views.post_toggle_status, name='post_toggle_status'),
    path('posts/<int:post>/delete/', views.post_delete, name='post_delete'),

    path('comments/', views.comment_list, name='comments'),
    path('comments/<int:comment_id>/toggle/', views.comment_toggle_approve, name='comment_toggle_approve'),
    path('comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),

    path('users/', views.user_list, name='users'),
    path('users/<int:user_id>/toggle/', views.user_toggle_active, name='user_toggle_active'),

    path('categories/', views.category_list, name='categories'),
    path('categories/<int:category_id>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:category_id>/delete/', views.category_delete, name='category_delete'),
]