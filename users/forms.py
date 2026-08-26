from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from blog.models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'content']
        

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']