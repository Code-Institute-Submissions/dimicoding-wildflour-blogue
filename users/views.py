from django.shortcuts import render
from django.views.generic import UpdateView  #DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'user.html'
    success_url = reverse_lazy('success_page')   
    
    def get_object(self, queryset=None):
        return self.request.user