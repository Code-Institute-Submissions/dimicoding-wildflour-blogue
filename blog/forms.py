from django import forms
from django.forms import ModelForm
from .models import Recipe, Category, Comment
from cloudinary.models import CloudinaryField
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


categories = Category.objects.all().values_list('title', 'title')
""" Loop trought the created categories"""
cat_list = []
for item in categories:
    cat_list.append(item)


class RecipeForm(forms.ModelForm):
    """ Create Recipe- Used from https://github.com/summernote/django-summernote """
    
    featured_image = CloudinaryField('image')

    class Meta:
        model = Recipe
        fields = ['title',
                  'slug',
                  'author',
                  'category',
                  'dificulty',
                  'total_time',
                  'featured_image',
                  'content',
                  'ingredients',
                  'instructions',
                  'exerpt',
                  'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'user', 'type':'hidden'}),
            'category': forms.Select(choices=cat_list, attrs={'class': 'form-control'}),
            'dificulty': forms.Select(attrs={'class': 'form-control'}),
            'total_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'ingredients': SummernoteWidget(attrs={'summernote': {'toolbar': [
                ['para', ['ul', 'paragraph']],
                ['font', ['bold', 'italic', 'underline']],
                ['insert', ['picture']]]}}),
            'instructions': SummernoteWidget(attrs={'summernote': {'toolbar': [
                ['para', ['ol', 'paragraph']],
                ['font', ['bold', 'italic', 'underline']],
                ['insert', ['picture']]]}}),
            'exerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '"Share a sneak peek of this delicious recipe! Write a short and catchy excerpt that will make others want to try it out."'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    '''Edit Recipe'''
    featured_image = CloudinaryField('image')

    class Meta:
        model = Recipe
        fields = ['title',
                  'slug',
                  'category',
                  'dificulty',
                  'total_time',
                  'featured_image',
                  'content',
                  'ingredients',
                  'instructions',
                  'exerpt',
                  'status']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cat_list, attrs={'class': 'form-control'}),
            'dificulty': forms.Select(attrs={'class': 'form-control'}),
            'total_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'ingredients': SummernoteWidget(attrs={'summernote': {'toolbar': [
                ['para', ['ul', 'paragraph']],
                ['font', ['bold', 'italic', 'underline']],
                ['insert', ['picture']]]}}),
            'instructions': SummernoteWidget(attrs={'summernote': {'toolbar': [
                ['para', ['ol', 'paragraph']],
                ['font', ['bold', 'italic', 'underline']],
                ['insert', ['picture']]]}}),
            'exerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '"Share a sneak peek of this delicious recipe! Write a short and catchy excerpt that will make others want to try it out."'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
