from django.db import models



class Help(models.Model):
    content = models.TextField()
    project_id = models.ForeignKey('Projects', on_delete=models.CASCADE)
    author_id = models.ForeignKey('GearHead', on_delete=models.CASCADE)
    