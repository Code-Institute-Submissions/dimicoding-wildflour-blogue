from django.urls import path
#from . import views
from .views import HomeView, FirstRecipeView

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('recipe/<int:pk>', FirstRecipeView.as_view(), name="first_recipe"),
]