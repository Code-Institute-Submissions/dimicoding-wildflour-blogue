from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Recipe


#def home(request):
#   return render(request, 'base.html', {})


class HomeView(ListView):
    model = Recipe
    template_name = "list-view.html"
    

class FirstRecipeView(DetailView):
    model = Recipe
    template_name = "first-recipe.html"


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = "create.html"
    fields = '__all__'


def test(request):
    return render(request, 'index.html')
