from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms


class EditUserForm(UserChangeForm):
    """User area, edit profile"""

    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "type": "hidden"}),
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exclude(
                pk=self.instance.pk).exists():
            raise ValidationError("Email already in use.")
        return email
