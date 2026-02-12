# blog/views.py

from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required

def blog_index(request):
    posts = Post.objects.filter(status="published").order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

@staff_member_required
def preview_draft(request):
    post = get_object_or_404(Post, pk=request.GET.get("pk"))
    context = {
        "post": post,
    }
    return render(request, "blog/preview.html", context)

def search_posts(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query),
            status="published"
        ).order_by("-created_on")
    else:
        posts = Post.objects.none()
    context = {
        "posts": posts,
        "query": query,
    }
    return render(request, "blog/search_results.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__iexact=category,
        status="published"
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get_object_or_404(pk=pk, status="published")
    context = {
        "post": post,
    }
    return render(request, "blog/detail.html", context)

def about(request):
    return render(request, 'blog/about.html')