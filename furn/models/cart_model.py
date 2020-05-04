from django.db import models
from django.contrib.auth.models import User

class cart(models.Model):
    user_id = models.IntegerField(blank=False)
    product_id = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.product_id)
