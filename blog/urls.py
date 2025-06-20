# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("search/", views.search_posts, name="blog_search"),
    path("about/", views.about, name="blog_about"),
]