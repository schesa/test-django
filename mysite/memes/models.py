from django.db import models

# Create your models here.
class Meme(models.Model):
    boxes = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100)