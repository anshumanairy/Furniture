from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class ImageManager(models.Manager):
    def get_by_instance(self,instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        images = super(ImageManager,self).filter(object_id=object_id,content_type=content_type)
        return images


class Image(models.Model):
    img = models.ImageField(upload_to='images/')
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ImageManager()