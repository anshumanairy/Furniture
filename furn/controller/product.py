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
from furn.models.product_model import product_upload

@login_required(login_url='/')
def prod(request):
    return render(request,'product.html/',{})

def prod_detail(request,procode):
    obj = get_object_or_404(product_upload,product_code=procode)
    img = obj.get_images
    context = {
        'product' : obj,
        'images' : img,
    }
    print("##debug")
    print(obj,img)
    return render(request,'product.html/',context)
