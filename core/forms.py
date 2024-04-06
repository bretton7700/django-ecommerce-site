#creating users
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter username',
        'class': 'w-full py-4 px-6 rounded-xl bg-white border border-gray-500',
    }))
     
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter password',
        'class': 'w-full py-4 px-6 rounded-xl bg-white border border-gray-500 ',
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields =('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter username',
        'class': 'w-full py-4 px-6 rounded-xl !bg-white border border-gray-500',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Enter email',
        'class': 'w-full py-4 px-6 rounded-xl !bg-white border border-gray-500',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter password',
        'class': 'w-full py-4 px-6 rounded-xl !bg-white border border-gray-500',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'confirm  password',
        'class': 'w-full py-4 px-6 rounded-xl !bg-white border border-gray-500',
    }))