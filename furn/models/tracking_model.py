from django.db import models
from django.contrib.auth.models import User

class track_order(models.Model):
    tracking_id = models.CharField(max_length=10,null=True)
    order_id = models.CharField(max_length=10)

    def __str__(self):
        return self.tracking_id
