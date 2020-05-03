from django.db import models
from django.contrib.auth.models import User
from .image_model import Image

types = (
    ('a','Almirah'),
    ('b','Bed'),
    ('ch','Chair'),
    ('cl','Closet'),
    ('l','Lamp'),
    ('m','Mattress'),
    ('s','Sofa'),
    ('t','Table'),
)

# def images_directory_path(self, filename):
#     return 'Furniture_{0}/{1}/{2}'.format('Images',self.id, filename)

class product_upload(models.Model):
    product_code = models.SlugField(unique=True)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    quantity = models.IntegerField(default=0)
    crossed_price = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    furniture_type = models.CharField(max_length=8, choices=types)

    # dimensions in inch
    length = models.IntegerField(default=0)
    breadth = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.title
    @property
    def get_images(self):
        images = Image.objects.get_by_instance(self)
        return images