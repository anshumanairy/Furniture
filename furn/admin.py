from django.contrib import admin
from furn.models.register_model import user_detail
from furn.models.image_model import Image
from furn.models.product_model import product_upload
from django.contrib.auth.models import Permission
from django.contrib import admin

admin.site.register(Permission)
admin.site.register(user_detail)
admin.site.register(product_upload)
admin.site.register(Image)

