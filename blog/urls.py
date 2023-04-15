from django.urls import path
#from . import views
from .views import HomeView, TheRecipeView, CreateRecipeView, EditRecipeView
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('recipe/<int:pk>', TheRecipeView.as_view(), name="the_recipe"),
    path('create/', CreateRecipeView.as_view(), name="create_recipe"),
    path('recipe/edit/<int:pk>', EditRecipeView.as_view(), name="edit_recipe"),
]
