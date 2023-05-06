from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import UserEdit  # PassChangeView

urlpatterns = [
    path("edit_profile/", UserEdit.as_view(), name="edit_profile"),

]
