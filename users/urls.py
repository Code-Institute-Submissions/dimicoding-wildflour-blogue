from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import User

urlpatterns = [

    path('user/', User.as_view(), name="see_user"),
]