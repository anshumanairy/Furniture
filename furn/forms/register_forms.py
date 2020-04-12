from django import forms
from furn.models.register_model import user_detail
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username','password')


class profileForm(forms.ModelForm):

    class Meta():
        model = user_detail
        fields = ('name','gender','phone','email')
