from django import forms
from .models import Profile, User
from django.contrib.auth.forms import UserCreationForm


class SignUp(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Input a valid email address."
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]
