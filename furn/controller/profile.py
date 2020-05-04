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
from furn.models.register_model import user_detail
from furn.controller import display_picture
from furn.controller import floating_cart

@login_required(login_url='/')
def profile(request):
    profile_picture = display_picture.check_admin(request)
    # Floating Cart Content
    cart_products = floating_cart.cart_product(request)
    cart_images = floating_cart.cart_image(request)

    check = User.objects.get(id = request.user.id)
    username = request.user.username
    name = 'Admin'
    gender = 'm'
    mobile = ''
    email = ''
    if check.is_superuser == False:
        details = user_detail.objects.get(user_id = request.user.id)
        username = request.user.username
        name = details.name
        gender = details.gender
        mobile = details.phone
        email = details.email

    context = {
        'profile_picture' : profile_picture,
        'cart_products':cart_products,
        'cart_images':cart_images,
        'username':username,
        'name':name,
        'gender':gender,
        'mobile':mobile,
        'email':email,
    }
    return render(request,'profile.html/',context)
