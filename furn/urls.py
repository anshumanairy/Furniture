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

from furn.controller import returns
from furn.controller import track_order
from furn.controller import saved_address
from furn.controller import your_orders
from furn.controller import your_wishlist
from furn.controller import search


urlpatterns = [
    url(r'^$',register.reg,name="register"),
    url(r'^cart-page',cart.cart,name="cart-page"),
    url(r'^search',search.searchProduct,name="search"),
    # url(r'^cart',cart.bag,name="cart"),
    # url(r'^categories/(?P<category>[a-zA-Z0-9]+$)',categories.category,name="categories"),
    url(r'^categories',categories.category,name="categories"),
    url(r'^checkout',checkout.purchase,name="checkout"),
    url(r'^contact',contact.contact,name="contact"),
    url(r'^home',home.home,name="home"),
    url(r'^product/(?P<procode>[-a-zA-Z0-9_]+)',product.prod_detail,name="product_detail"),
    url(r'^profile',profile.profile,name="profile"),
    url(r'^admin',admin.admin,name="admin"),
    url(r'^returns',returns.returns,name="returns"),
    url(r'^track',track_order.track,name="track"),
    url(r'^address',saved_address.address,name="address"),
    url(r'^orders',your_orders.orders,name="orders"),
    url(r'^wishlist',your_wishlist.wishlist,name="wishlist"),
]
