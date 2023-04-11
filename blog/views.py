from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe


#def home(request):
#   return render(request, 'base.html', {})


class HomeView(ListView):
    model = Recipe
    template_name = "base.html"
    

class FirstRecipeView(DetailView):
    model = Recipe
    template_name = "first-recipe.html"