from django.shortcuts import render

# Create your views here.

def author_view(request):
    return render(request,'accounts/author.html')

def login_view(request):
    return render(request,'accounts/login.html')

def profile_view(request):
    return render(request,'accounts/profile.html')

def register_view(request):
    return render(request,'accounts/register.html')

def logout_view(request):
    pass