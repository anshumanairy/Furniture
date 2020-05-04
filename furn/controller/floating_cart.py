from django.shortcuts import render,redirect,get_object_or_404
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
# Model Imports
from furn.models.product_model import product_upload
from furn.models.image_model import ImageManager, Image
from furn.models.cart_model import cart
from furn.models.register_model import user_detail

@login_required(login_url='/')
def cart_product(request):
    cart_products=[]
    if(cart.objects.filter(user_id=request.user.id).exists()):
        cart_obj = cart.objects.filter(user_id=request.user.id)
        for ob in cart_obj:
            prod = product_upload.objects.get(id=ob.product_id)
            cart_products.append(prod)
    else:
        cart_products=''

    return cart_products

@login_required(login_url='/')
def cart_image(request):
    cart_images=[]
    if(cart.objects.filter(user_id=request.user.id).exists()):
        cart_obj = cart.objects.filter(user_id=request.user.id)
        for ob in cart_obj:
            prod = product_upload.objects.get(id=ob.product_id)
            cart_images.append((prod.get_images)[0])

    return cart_images
