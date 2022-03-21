from django.db import models

# Create your models here.

class Users(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField(max_length=245)
    username    = models.CharField(max_length=70)
    password    = models.CharField( max_length=50)
    address		= models.CharField(max_length=150)
    phone       = models.IntegerField()
    # pip install Pillow 
    foto        = models.ImageField(upload_to= 'userImage', default='image.png', height_field=None, width_field=None, max_length=100)