# blog/admin.py
# ignores for Pylance

from django.contrib import admin
from blog.models import Category, Comment, Post
from django.utils import timezone

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on', 'published_date')
    list_filter = ('status', 'created_on', 'published_date', 'categories')
    search_fields = ('title', 'body')
    ordering = ('-created_on',)
    
    actions = ['make_published', 'make_draft']
    
    def make_published(self, request, queryset):
        count = queryset.update(status='published', published_date=timezone.now())
        self.message_user(request, f'{count} posts marked as published.')
    make_published.short_description = 'Mark selected posts as published' # type: ignore
    
    def make_draft(self, request, queryset):
        count = queryset.update(status='draft')
        self.message_user(request, f'{count} posts marked as draft.')
    make_draft.short_description = 'Mark selected posts as draft' # type: ignore

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

