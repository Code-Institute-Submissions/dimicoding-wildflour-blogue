from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Recipe
from .forms import RecipeForm


class HomeView(ListView):
    model = Recipe
    template_name = "list-view.html"
    

class FirstRecipeView(DetailView):
    model = Recipe
    template_name = "first-recipe.html"


class CreateRecipeView(CreateView):
    form_class = RecipeForm
    template_name = 'create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
       
        return response


# #class CreateRecipeView(CreateView):
#     model = Recipe
#     template_name = "create.html"
#     fields = '__all__'

