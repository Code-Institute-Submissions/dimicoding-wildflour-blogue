from django.urls import path
#from . import views
from .views import HomeView, FirstRecipeView, test
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('home/', views.home, name='home'),
    path('recipe/', HomeView.as_view(), name="home"),
    path('recipe/<int:pk>', FirstRecipeView.as_view(), name="first_recipe"),
    path('test/', test, name='mytest'),


]