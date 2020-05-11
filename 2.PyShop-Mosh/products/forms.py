from django import forms
from .models import Product, UserProfileInfo
from django.contrib.auth.models import User



class PostProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')