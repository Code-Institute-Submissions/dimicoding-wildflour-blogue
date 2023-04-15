from django import forms
from django.forms import ModelForm
from .models import Recipe
from cloudinary.models import CloudinaryField
from django_summernote.widgets import SummernoteWidget


class RecipeForm(forms.ModelForm):
    """ Used from https://github.com/summernote/django-summernote """
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['likes',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'dificulty': forms.Select(attrs={'class': 'form-control'}),
            'total_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'exerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def form_valid(self, form):
        form.instance.title = slugify(form.cleaned_data['slug'])
        return super().form_valid(form)

