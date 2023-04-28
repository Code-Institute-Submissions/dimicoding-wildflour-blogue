from django.contrib import admin
from .models import Recipe, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Add fields for Recipe post in admin panel
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status',)
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Add fields for Category in admin panel
    """
    list_display = ['title', 'image', 'description']
    search_fields = ['title', 'description']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for comments in admin panel
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# @admin.register(Comment)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post')