from django import forms
from django.forms import ModelForm
from .models import Recipe
from django_summernote.widgets import SummernoteWidget


class RecipeForm(forms.ModelForm):
    """ Used from https://github.com/summernote/django-summernote """
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }
