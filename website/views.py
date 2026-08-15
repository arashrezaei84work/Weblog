from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from website.forms import ContactForm
from django.contrib import messages

# Create your views here.

def home(request):
    post = Post.objects.filter(status=1)
    return render(request, 'website/home.html',{'posts':post})

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request,messages.SUCCESS,'تیکت شما ثبت شد.')
            form.save()
        else:
            messages.add_message(request,messages.ERROR,'تیکت ثبت نشد درخواست خود را دوباره بررسی کنید.')
    form = ContactForm()
    return render(request, 'website/contact.html',{'form':form})