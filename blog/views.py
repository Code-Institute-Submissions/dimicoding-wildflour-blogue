from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe, Category
from .forms import RecipeForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Recipe
    template_name = "list-view.html"
    ordering = ['-created_recipe']


def Category(request, cat):
    """
    Renders the categories page
    """
    return render(
        request,
        'categories.html',
        {
            "cat": "cat",
        })

# def CategoryView(request, cats):
#     """
#     Renders the posts filtered by categories
#     """
#     category_posts = Post.objects.filter(
#         category__title__contains=cats, status=1)
#     return render(request, 'categories.html', {
#         'cats': cats.title(), 'category_posts': category_posts})


class TheRecipeView(DetailView):
    model = Recipe
    template_name = "the-recipe.html"


class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create.html'


class EditRecipeView(UpdateView):
    model = Recipe
    form_class = EditForm
    template_name = 'edit-recipe.html'


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete-recipe.html'
    success_url = reverse_lazy('home')
