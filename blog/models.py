from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True, blank=True)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/',default='default.webp')
    post_view = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User,related_name='liked_posts',blank=True)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('published_date',)

    def __str__(self):
        return f"{self.id}-{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title, allow_unicode=True)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f"{base_slug}-{counter}"
            self.slug = slug

            
        if self.status and not self.published_date:
            self.published_date = timezone.now()


        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'slug':self.slug})
    
class Comment(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    likes = models.ManyToManyField(User,related_name='liked_comments',blank=True)
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.name}-{self.post_id}"

