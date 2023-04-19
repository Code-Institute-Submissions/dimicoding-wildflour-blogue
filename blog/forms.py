from django import forms
from django.forms import ModelForm
from .models import Recipe, Category
from cloudinary.models import CloudinaryField
from django_summernote.widgets import SummernoteWidget

categories = Category.objects.all().values_list('name', 'name')
cat_list = []
for item in categories:
    cat_list.append(item)


class RecipeForm(forms.ModelForm):
    """ Used from https://github.com/summernote/django-summernote """
    class Meta:
        model = Recipe
        fields = ['title',
                  'slug',
                  'author',
                  'category',
                  'dificulty',
                  'total_time',
                  'content',
                  'exerpt',
                  'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cat_list, attrs={'class': 'form-control'}),
            'dificulty': forms.Select(attrs={'class': 'form-control'}),
            'total_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'exerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title',
                  'slug',
                  'category',
                  'dificulty',
                  'total_time',
                  'content',
                  'exerpt',
                  'status']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'dificulty': forms.Select(attrs={'class': 'form-control'}),
            'total_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'exerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }