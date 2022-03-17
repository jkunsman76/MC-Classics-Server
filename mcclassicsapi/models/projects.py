from django.db import models

def upload_path(instance,filename):
    """photo uploading path"""
    return '/'.join(['image',str(instance.title),filename])

class Projects(models.Model):
    gear_head = models.ForeignKey('GearHead', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    details = models.TextField()
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    