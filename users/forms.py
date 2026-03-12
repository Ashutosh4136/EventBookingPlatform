from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'role',
            'password1',
            'password2'
        ]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'profile_picture',
            'phone',
            'bio'
        ]