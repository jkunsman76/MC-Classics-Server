from rest_framework import serializers
from mcclassicsapi.models import Event
# from mcclassicsapi.serializers import GearHeadSerializer



class EventSerializer(serializers.ModelSerializer):
    # creator = GearHeadSerializer()
    class Meta:
        model = Event
        fields = ('id', 'type', 'creator',
          'description', 'date', 'attendees',
          'joined')
        depth = 1
         
class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['type',
          'description', 'date']
        