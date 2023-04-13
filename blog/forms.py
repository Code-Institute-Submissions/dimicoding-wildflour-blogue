from django import forms
from django.forms import ModelForm
from .models import Recipe
from django_summernote.widgets import SummernoteWidget


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }
