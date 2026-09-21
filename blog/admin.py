from django.contrib import admin
from blog.models import Category,Post, Comment
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','post_view','status')
    list_filter = ('status',)
    search_fields = ('title','author__username','content')

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','post_id','approved','created_date')
    list_filter = ('approved',)

