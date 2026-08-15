from django.urls import path
from accounts import views
app_name = 'accounts'

urlpatterns = [
    path('author/',views.author_view,name='author'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.register_view,name='register'),
    path('login/profile/',views.profile_view,name='profile'),
    path('logout/',views.logout_view,name='logout'),
]
