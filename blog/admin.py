# blog/admin.py
# ignores for Pylance

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from blog.models import Category, Comment, Post
from django.utils import timezone

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on', 'published_date')
    list_filter = ('status', 'created_on', 'published_date', 'categories')
    search_fields = ('title', 'body')
    ordering = ('-created_on',)
    filter_horizontal = ('categories',)
    actions = ['make_published', 'make_draft']
    
    def make_published(self, request, queryset):
        count = queryset.update(status='published', published_date=timezone.now())
        self.message_user(request, f'{count} posts marked as published.')
    make_published.short_description = 'Mark selected posts as published' # type: ignore
    
    def make_draft(self, request, queryset):
        count = queryset.update(status='draft')
        self.message_user(request, f'{count} posts marked as draft.')
    make_draft.short_description = 'Mark selected posts as draft' # type: ignore

    readonly_fields = ('preview_link',)

    def preview_link(self, obj):
        if obj.pk:
            url = reverse('blog_preview') + f'?pk={obj.pk}'
            return format_html(
                '<a href="{}" target="_blank">Preview Post</a>',
                url
            )
        return '-'
    preview_link.short_description = 'Preview' # type: ignore

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

