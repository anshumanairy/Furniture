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
from furn.models.image_model import ImageManager, Image
from furn.controller import display_picture

@login_required(login_url='/')
def prod(request):
    # procode set to 1, which is according to the product in my db, change accordingly when testing
    profile_picture = display_picture.check_admin(request)
    product = product_upload.objects.get(product_code=1)
    image = Image.objects.filter(object_id=1)
    images = []
    main_image=image[0].img
    for i in image:
        images.append(i.img)
    return render(request,'product.html/',{'profile_picture':profile_picture,'product':product,'images':images,'main_image':main_image})

def prod_detail(request,procode):
    profile_picture = display_picture.check_admin(request)
    obj = get_object_or_404(product_upload,product_code=procode)
    img = obj.get_images

    # product = product_upload.objects.get(product_code=procode)
    # image = Image.objects.filter(object_id=procode)
    # images = []
    # main_image=image[0].img
    # for i in image:
    #     images.append(i.img)

    context = {
        'profile_picture' : profile_picture,
        # 'product':product,
        'product':obj,
        # 'images':images,
        'images':img,
        'main_image':img[0],
    }
    # print("##debug")
    print(obj,img)
    return render(request,'product.html/',context)
