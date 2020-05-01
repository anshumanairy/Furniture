from django.urls import path
from furn.controller import home
from furn.controller import cart
from furn.controller import categories
from furn.controller import checkout
from furn.controller import contact
from furn.controller import product
from furn.controller import profile
from furn.controller import register
from furn.controller import admin
from django.conf.urls import url,include

urlpatterns = [
    url(r'^$',register.reg,name="register"),
    url(r'^cart',cart.bag,name="cart"),
    url(r'^categories',categories.category,name="categories"),
    url(r'^checkout',checkout.purchase,name="checkout"),
    url(r'^contact',contact.contact,name="contact"),
    url(r'^home',home.base,name="home"),
    url(r'^product',product.prod,name="product"),
    url(r'^profile',profile.profile,name="profile"),
    url(r'^admin',admin.admin,name="admin"),
]
