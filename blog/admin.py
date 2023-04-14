from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status',)
    search_fields = ['title', 'content']
    summernote_fields = ('body')