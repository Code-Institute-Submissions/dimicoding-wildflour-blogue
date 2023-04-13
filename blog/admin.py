from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

