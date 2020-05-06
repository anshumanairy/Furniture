from django.db import models
from django.contrib.auth.models import User
from .product_model import product_upload

class Cart_items(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(product_upload,on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def net_price(self):
        price = self.product.selling_price * self.quantity
        return price