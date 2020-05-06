from django.db import models
from django.contrib.auth.models import User
from .cart_model import Cart_items

gender = (
    ('m','Male'),
    ('f','Female'),
    ('o','Other')
)

class user_detail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=gender, default="Male")
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='Profile', blank=True)

    def __str__(self):
        return self.user.email

    def cart_items(self):
        items = Cart_items.objects.filter(user=self.user)
        print(items)
        return items

    def count_cart(self):
        val = len(self.cart_items())
        print(val)
        return val