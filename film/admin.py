from django.contrib import admin
from .models import BlogPost, Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_date', 'summary')
    list_filter = ('author', 'published_date', 'updated_date')
    search_fields = ('title', 'content', 'author__username', 'summary')
    date_hierarchy = 'published_date'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'post', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date', 'author')
    search_fields = ('text', 'author__username', 'post__title')
    actions = ['approve_comments']


