from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import UserUpdateView

urlpatterns = [

    path('user/', UserUpdateView.as_view(), name="see_user"),
]