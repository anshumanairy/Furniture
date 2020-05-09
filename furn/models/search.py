from django.db import models
from django.contrib.auth.models import User

class SearchQuery(models.Model):
    query = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']