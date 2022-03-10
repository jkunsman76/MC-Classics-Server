from django.db import models

class EventAttendees(models.Model):
    gear_head = models.ForeignKey("GearHead", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    