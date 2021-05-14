from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image', 'header']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',]

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(max_length=300, blank=True)
    image = forms.ImageField(upload_to='images/profile')
    header = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ['bio', 'image', 'header']
