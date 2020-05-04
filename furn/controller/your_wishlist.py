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
from furn.controller import display_picture
from furn.controller import floating_cart

@login_required(login_url='/')
def wishlist(request):
    profile_picture = display_picture.check_admin(request)
    # Floating Cart Content
    cart_products = floating_cart.cart_product(request)
    cart_images = floating_cart.cart_image(request)

    context = {
        'profile_picture' : profile_picture,
        'cart_products':cart_products,
        'cart_images':cart_images
    }
    return render(request,'your_wishlist.html/',context)
