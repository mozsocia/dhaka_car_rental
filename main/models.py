from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class FrontProfile(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    nid_image = models.ImageField(upload_to='nid_images/')
    profile_image = models.ImageField(upload_to='profile_images/', default='profile/no_profile.jpg')
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)

