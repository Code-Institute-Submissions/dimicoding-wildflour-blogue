from django.shortcuts import render, get_object_or_404, reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views import generic, View
from .models import Recipe, Category, Comment
from .forms import RecipeForm, EditForm, CommentForm, ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def index(request):
    """Display the index page"""

    # Dropdown menu list
    cat_list = Category.objects.all()
    cat_list_view = Category.objects.all().values("title", "image")

    return render(
        request, "index.html",
        {"cat_list": cat_list, "cat_list_view": cat_list_view}
    )


def contact(request):
    # Dropdown menu list
    cat_list = Category.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = "Client Contant Form"
            body = f"Name:{name}\nEmail:{email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                body,
                email,
                ["dimo4ka1@hotmail.com"],
                fail_silently=False,
            )
            return render(request, "contact.html", {"name": name})
    else:
        form = ContactForm()
    return render(
        request,
        "contact.html", {"form": form, "cat_list": cat_list})


def about(request):
    """Dropdown menu list"""
    cat_list = Category.objects.all()

    return render(request, "about.html", {"cat_list": cat_list})


def RecipeLike(request, pk):
    """Defining Like View"""

    post = get_object_or_404(Recipe, id=request.POST.get("recipe_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse("the_recipe", args=[str(pk)]))


class HomeView(ListView):
    """
    Accessible from "blog" navbar, displays all recipes
    """

    model = Recipe
    template_name = "list-view.html"
    ordering = ["-created_recipe"]
    paginate_by = 8

    # Dropdown menu list
    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_list"] = cat_list
        return context


def CategoryListView(request):
    """
    Displays a page with all categories of the blog
    """
    # Dropdown menu list
    cat_list = Category.objects.all()
    cat_list_view = Category.objects.all().values("title", "image")
    return render(
        request,
        "categories-page.html",
        {"cat_list_view": cat_list_view, "cat_list": cat_list},
    )


def CategoryList(request, cat):
    """
    Displays the page with recipes of the specific Category
    """
    # Dropdown menu list
    cat_list = Category.objects.all()
    cat_list_view = Category.objects.all().values("title", "image")
    recipe_category = Recipe.objects.filter(
        category=cat.replace("-", " ")).order_by(
        "-created_recipe"
    )
    return render(
        request,
        "category.html",
        {
            "cat": cat.title().replace("-", " "),
            "recipe_category": recipe_category,
            "cat_list_view": cat_list_view,
            "cat_list": cat_list,
        },
    )


class TheRecipeView(DetailView):
    model = Recipe
    template_name = "the-recipe.html"

    def get_context_data(self, *args, **kwargs):
        """Dropdown menu list"""
        cat_list = Category.objects.all()
        context = super(TheRecipeView, self).get_context_data(*args, **kwargs)

        """ Indentify the specific post place"""
        place = get_object_or_404(Recipe, id=self.kwargs["pk"])
        number_likes = place.number_likes()

        comments = Comment.objects.filter(approved=True).order_by("created_on")

        if self.request.user.is_authenticated:
            context["comment_form"] = CommentForm(instance=self.request.user)

        liked = False
        if place.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_list"] = cat_list
        context["number_likes"] = number_likes
        context["liked"] = liked
        context["comments"] = comments
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            body=request.POST.get("body"),
            name=self.request.user,
            post=self.get_object(),
        )
        new_comment.save()
        messages.success(
            request,
            "Your comment was successfully submitted! Awaiting approval."
        )
        return self.get(self, request, *args, **kwargs)


class CreateRecipeView(SuccessMessageMixin, CreateView):
    """
    CRUD Functionality
    Ability for the user to create a recipe
    """

    model = Recipe
    form_class = RecipeForm
    template_name = "create.html"
    success_message = "Recipe successfully created!"

    # Dropdown menu list
    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(CreateRecipeView, self).get_context_data(
            *args, **kwargs)
        context["cat_list"] = cat_list
        return context


class EditRecipeView(SuccessMessageMixin, UpdateView):
    model = Recipe
    form_class = EditForm
    template_name = "edit-recipe.html"
    success_message = "Your Recipe was successfully updated!"


class DeleteRecipeView(SuccessMessageMixin, DeleteView):
    model = Recipe
    template_name = "delete-recipe.html"
    success_url = reverse_lazy("home")
    success_message = "Your Recipe was successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteRecipeView, self).delete(request, *args, **kwargs)
