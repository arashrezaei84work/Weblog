from django.urls import path
from website.views import home, contact, about

app_name = 'website'

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
]
