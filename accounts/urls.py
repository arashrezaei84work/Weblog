from django.urls import path
from accounts import views
app_name = 'accounts'

urlpatterns = [
    path('author/',views.author_view,name='author'),
    path('login/',views.login_view,name='login'),
    path('author/',views.register_view,name='register'),
    path('profile/',views.profile_view,name='profile'),
    path('logout/',views.logout_view,name='logout'),
]
