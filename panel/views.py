from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Q
from django.views.decorators.http import require_POST
from blog.models import Post, Comment, Category


@staff_member_required
def dashboard(request):
    context = {
        'total_posts': Post.objects.count(),
        'published_posts': Post.objects.filter(status=True).count(),
        'pending_posts': Post.objects.filter(status=False).count(),
        'total_comments': Comment.objects.count(),
        'pending_comments': Comment.objects.filter(approved=False).count(),
        'total_users': User.objects.count(),
        'total_categories': Category.objects.count(),
        'recent_posts': Post.objects.select_related('author').order_by('-created_date')[:5],
        'recent_comments': Comment.objects.select_related('post').order_by('-created_date')[:5],
    }
    return render(request, 'panel/dashboard.html', context)


@staff_member_required
def post_list(request):
    q = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', '')

    posts = Post.objects.select_related('author').all()
    if q:
        posts = posts.filter(Q(title__icontains=q))
    if status_filter == 'published':
        posts = posts.filter(status=True)
    elif status_filter == 'pending':
        posts = posts.filter(status=False)

    return render(request, 'panel/posts.html', {
        'posts': posts, 'q': q, 'status_filter': status_filter,
    })


@staff_member_required
def post_toggle_status(request, post):
    post = get_object_or_404(Post, id=post)
    post.status = not post.status
    post.save()
    messages.success(request, f'وضعیت پست «{post.title}» تغییر کرد.')
    return redirect('panel:posts')


@staff_member_required
def post_delete(request, post):
    post = get_object_or_404(Post, id=post)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'پست حذف شد.')
        return redirect('panel:posts')
    return render(request, 'panel/confirm_delete.html', {
        'title': post.title, 'cancel_url': 'panel:posts',
    })


@staff_member_required
def comment_list(request):
    status_filter = request.GET.get('status', '')
    comments = Comment.objects.select_related('post').all()
    if status_filter == 'approved':
        comments = comments.filter(approved=True)
    elif status_filter == 'pending':
        comments = comments.filter(approved=False)
    return render(request, 'panel/comments.html', {
        'comments': comments, 'status_filter': status_filter,
    })


@staff_member_required
def comment_toggle_approve(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.approved = not comment.approved
    comment.save()
    messages.success(request, 'وضعیت نظر بروزرسانی شد.')
    return redirect('panel:comments')


@staff_member_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'نظر حذف شد.')
        return redirect('panel:comments')
    return render(request, 'panel/confirm_delete.html', {
        'title': comment.name, 'cancel_url': 'panel:comments',
    })


@staff_member_required
def user_list(request):
    users = User.objects.annotate(posts_count=Count('post')).order_by('-date_joined')
    return render(request, 'panel/users.html', {'users': users})


@staff_member_required
def user_toggle_active(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user == request.user:
        messages.error(request, 'نمی‌تونی وضعیت حساب خودت رو تغییر بدی!')
        return redirect('panel:users')
    user.is_active = not user.is_active
    user.save()
    messages.success(request, 'وضعیت کاربر بروزرسانی شد.')
    return redirect('panel:users')


@staff_member_required
def category_list(request):
    categories = Category.objects.annotate(posts_count=Count('post')).order_by('name')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            Category.objects.create(name=name)
            messages.success(request, 'دسته‌بندی اضافه شد.')
        else:
            messages.error(request, 'نام دسته‌بندی نمی‌تونه خالی باشه.')
        return redirect('panel:categories')
    return render(request, 'panel/categories.html', {'categories': categories})


@staff_member_required
@require_POST
def category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            category.name = name
            category.save()
            messages.success(request, 'دسته‌بندی ویرایش شد.')
        return redirect('panel:categories')


@staff_member_required
def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'دسته‌بندی حذف شد.')
    return redirect('panel:categories')