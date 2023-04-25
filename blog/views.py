from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic, View
from .models import Recipe, Category, Comment
from .forms import RecipeForm, EditForm, CommentForm
from django.urls import reverse_lazy


def RecipeLike(request, pk):

    """Defining Like View"""

    post = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('the_recipe', args=[str(pk)]))


class HomeView(ListView):
    model = Recipe
    template_name = "list-view.html"
    ordering = ['-created_recipe']
    paginate_by = 6

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

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all() #Dropdown menu list 
        context = super(TheRecipeView, self).get_context_data(*args, **kwargs)

        """ Indentify the specific post place"""
        place = get_object_or_404(Recipe, id=self.kwargs['pk'])
        number_likes = place.number_likes()

        comments = Comment.objects.filter(approved=True).order_by('created_on')

        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)

        liked = False
        if place.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_list"] = cat_list
        context["number_likes"] = number_likes
        context["liked"] = liked
        context["comments"] = comments
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'), name=self.request.user, post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


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


