from django.db import models
from django.contrib.auth.models import User




class GearHead(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    profile_img = models.ImageField(blank=True, null=True, upload_to='profilepics')
    # username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="username")
    # first_name = models.OneToOneField(User, on_delete=models.CASCADE related_name="first_name")
    # last_name = models.OneToOneField(User, on_delete=models.CASCADE related_name="last_name")
    # email = models.OneToOneField(User, on_delete=models.CASCADE related_name="email")