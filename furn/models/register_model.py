from django.db import models
from django.contrib.auth.models import User

gender = (
    ('m','Male'),
    ('f','Female'),
    ('o','Other')
)

class user_detail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=gender)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.user.email
