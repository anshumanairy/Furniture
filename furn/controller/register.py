from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.template.response import TemplateResponse
from datetime import timedelta
from django.db.models import Sum
import datetime
from django.contrib import messages
from django.contrib.auth.hashers import check_password
import base64
import hashlib
import hmac
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.utils.timezone import utc
from django.utils import timezone
from furn.forms.register_forms import UserForm, profileForm
from furn.models.register_model import user_detail


def reg(request):
    # Login
    if request.method == 'GET':
        if 'login_button' in request.GET:
            username = request.GET.get('username')
            password = request.GET.get('password')
            if User.objects.filter(username=username).exists() == True:
                user = authenticate(username = username, password=password)
                if user:
                    login(request,user)
                    return redirect('home')
                else:
                    messages.info(request, 'Invalid Account Details! Please Check!')
            else:
                messages.info(request, 'Invalid Account Details! Please Check!')

    # Register
    if request.method == 'POST':
        if 'register_button' in request.POST:
            user_form = UserForm(request.POST)
            profile_form = profileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save(commit=False)
                profile = profile_form.save(commit=False)
                profile.user = user
                user.email = profile.email
                # Password Hasing Encryption of Django. Works in combination with the password hashers in settings.py
                user.set_password(user.password)
                user.save()
                profile.save()
                return redirect('/')
    else:
        user_form = UserForm()
        profile_form = profileForm()
    return render(request,'register.html/',{'user_form':user_form , 'profile_form':profile_form})
