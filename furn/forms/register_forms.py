from django import forms
from furn.models.register_model import user_detail
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta():
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input--style-3', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'input--style-3', 'placeholder': 'Password'}),
        }
        fields = ('username','password')


class profileForm(forms.ModelForm):
    class Meta():
        model = user_detail
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input--style-3', 'placeholder': 'Name'}),
            'phone': forms.TextInput(attrs={'class': 'input--style-3', 'placeholder': 'Phone Number'}),
            'email': forms.TextInput(attrs={'class': 'input--style-3', 'placeholder': 'Email'}),
        }
        fields = ('name','gender','phone','email')
