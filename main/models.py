from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class FrontProfile(models.Model):
    full_name = models.CharField(max_length=255)
    NID_number = models.IntegerField()
    nid_image_front = models.ImageField(upload_to='nid_images/')
    nid_image_back = models.ImageField(upload_to='nid_images/')
    profile_image = models.ImageField(upload_to='profile_images/', default='no_profile.jpg')
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)

class MyModel(models.Model):
    content = models.TextField()