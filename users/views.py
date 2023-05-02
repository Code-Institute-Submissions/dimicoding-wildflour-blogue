from django.shortcuts import render
from django.views.generic import UpdateView  #DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm  #PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditUserForm


# class PassChangeView(PasswordChangeView):
#     form_class = PasswordChangeForm
#     success_url = reverse_lazy('password_success')


# def password_success(request):
#     return render(request, 'account/password_success.html', {})


class UserEdit(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'user.html'
    success_url = reverse_lazy('edit_profile')   
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your profile was successfully updated!')
        return response
