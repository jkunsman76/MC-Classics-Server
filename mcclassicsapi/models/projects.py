from django.db import models


class Projects(models.Model):
    gear_head = models.ForeignKey('GearHead', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField( upload_to='classicphotos', height_field=None,
        width_field=None, max_length=None, null=True)
    details = models.TextField()
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    