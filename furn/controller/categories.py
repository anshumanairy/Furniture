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
from furn.models.product_model import product_upload
from furn.models.image_model import ImageManager, Image

@login_required(login_url='/')
def category(request,search_text):
    profile_picture = display_picture.check_admin(request)
    # Floating Cart Content
    obj = product_upload.objects.all()
    products = []
    images = []
    for product in obj:
        products.append(product)
        img = product.get_images
        images.append(img[0])


    context = {
        'profile_picture' : profile_picture,
        'products':products,
        'images':images,
    }

    return render(request,'categories.html/',context)
