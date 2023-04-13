from django.urls import path
#from . import views
from .views import HomeView, FirstRecipeView, CreateRecipeView, test
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('home/', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('recipe/<int:pk>', FirstRecipeView.as_view(), name="first_recipe"),
    path('create/', CreateRecipeView.as_view(), name="create_recipe"),
    path('test/', test, name='mytest'),


]