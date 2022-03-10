from django.db import models



class Projects(models.Model):
    
    gear_head = models.ForeignKey('GearHead', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    image = models.URLField(default=None)
    details = models.TextField()
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField()