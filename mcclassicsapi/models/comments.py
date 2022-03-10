from django.db import models



class Comments(models.Model):
    content = models.TextField()
    project = models.ForeignKey('Projects', on_delete=models.CASCADE)
    author = models.ForeignKey('GearHead', on_delete=models.CASCADE)
    @property
    def is_owner(self):
        """is owner"""
        return self.__is_owner

    @is_owner.setter
    def is_owner(self, value):
        self.__is_owner = value
        