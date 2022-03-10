from django.db import models



class Help(models.Model):
    content = models.TextField()
    project = models.ForeignKey('Projects', on_delete=models.CASCADE)
    author = models.ForeignKey('GearHead', on_delete=models.CASCADE)
    