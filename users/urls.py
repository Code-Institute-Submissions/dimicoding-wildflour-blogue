from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import UserEdit # PassChangeView

urlpatterns = [

    path('edit_profile/', UserEdit.as_view(), name="edit_profile"),
    #path('password/', PassChangeView.as_view(template_name='account/changepass.html')),
    #path('password_success/', views.password_success, name='password_success'),
]