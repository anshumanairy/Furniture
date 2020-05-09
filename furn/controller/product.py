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
from furn.models.cart_model import Cart_items
from furn.models.register_model import user_detail
# Controller View Imports
from furn.controller import display_picture

@login_required(login_url='/')
def prod_detail(request,procode):

    # Product Details
    obj = get_object_or_404(product_upload,product_code=procode)
    img = obj.get_images

    item = Cart_items.objects.filter(user=request.user,product=obj)
    print(item.exists())
    if item.exists():
        already_added = True
    else:
        already_added = False
    # Add to Cart
    if request.method=='GET':
        if 'add_to_cart' in request.GET:
            cart_item = Cart_items(user=request.user,product=obj,quantity=request.GET.get('quantity_to_add'))
            cart_item.save()
            return redirect(obj)


    context = {
        'product':obj,
        'images':img,
        'main_image':img[0],
        'already_added':already_added,
    }

    return render(request,'product.html/',context)
