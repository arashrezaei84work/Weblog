from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile/')
                
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)
    else:
        redirect('/')

def author_view(request):
    return render(request,'accounts/author.html')

def profile_view(request):
    return render(request,'accounts/profile.html')

def register_view(request):
    return render(request,'accounts/register.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')