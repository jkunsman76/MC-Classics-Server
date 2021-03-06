from django.db import models



class Event(models.Model):
    type = models.CharField(max_length=50)
    creator = models.ForeignKey("GearHead", on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    attendees = models.ManyToManyField("GearHead", through="EventAttendees", related_name="attending")
    
    @property
    def joined(self):
        """join event"""
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
        