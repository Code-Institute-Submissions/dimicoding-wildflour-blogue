from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from .views import HomeView, TheRecipeView, CreateRecipeView, EditRecipeView, DeleteRecipeView, CategoryList, CategoryListView, RecipeLike


urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', HomeView.as_view(), name="home"),
    path('recipe/<int:pk>', TheRecipeView.as_view(), name="the_recipe"),
    path('create/', CreateRecipeView.as_view(), name="create_recipe"),
    path('recipe/edit/<int:pk>', EditRecipeView.as_view(), name="edit_recipe"),
    path('recipe/<int:pk>/delete', DeleteRecipeView.as_view(), name="delete_recipe"),
    path('categories/', CategoryListView, name="categories"),
    path('category/<str:cat>/', CategoryList, name="category"),
    path('like/<int:pk>', RecipeLike, name="recipe_like"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)