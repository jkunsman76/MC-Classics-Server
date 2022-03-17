from django.db import models
from django.contrib.auth.models import User


def upload_path2(instance,filename):
    """photo uploading path"""
    return '/'.join(['profile_img',str(instance.user),filename])

class GearHead(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    profile_img = models.ImageField(blank=True, null=True, upload_to=upload_path2)
   