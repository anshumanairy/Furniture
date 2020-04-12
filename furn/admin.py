from django.contrib import admin
from furn.models.register_model import user_detail
from django.contrib.auth.models import Permission
from django.contrib import admin

admin.site.register(Permission)
admin.site.register(user_detail)
