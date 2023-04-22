from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Recipe, Category
from .forms import RecipeForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Recipe
    template_name = "list-view.html"
    ordering = ['-created_recipe']

    # Dropdown menu list 
    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_list"] = cat_list
        return context


def CategoryListView(request):
    """
    Displays a page with all categories in the blog 
    """
    cat_list_view = Category.objects.all().values('title', 'image')
    return render(
        request,
        'categories-page.html',
        {
            "cat_list_view": cat_list_view,
        })


def CategoryList(request, cat):
    """
    Displays the categories page
    """
    recipe_category = Recipe.objects.filter(category=cat.replace('-', ' '))
    return render(
        request,
        'category.html',
        {
            "cat": cat.title().replace('-', ' '),
            "recipe_category": recipe_category,
        })


class TheRecipeView(DetailView):
    model = Recipe
    template_name = "the-recipe.html"

    # Dropdown menu list 
    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(TheRecipeView, self).get_context_data(*args, **kwargs)

        """ Indentify the specific post place"""

        place = get_object_or_404(Recipe, id=self.kwargs['pk'])
        number_likes = place.number_likes()
        context["cat_list"] = cat_list
        context["number_likes"] = number_likes
        return context


def RecipeLike(request, pk):
    post = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('the_recipe', args=[str(pk)]))


class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create.html'

    # Dropdown menu list 
    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(CreateRecipeView, self).get_context_data(*args, **kwargs)
        context["cat_list"] = cat_list
        return context


class EditRecipeView(UpdateView):
    model = Recipe
    form_class = EditForm
    template_name = 'edit-recipe.html'


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete-recipe.html'
    success_url = reverse_lazy('home')


