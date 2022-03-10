from django.db import models



class Event(models.Model):
    type = models.CharField(max_length=50)
    creator = models.ForeignKey("GearHead", on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    attendees = models.ManyToManyField("GearHead", through="EventAttendees", related_name="attending")
    