from rest_framework import serializers
from mcclassicsapi.models import Event



class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'type', 'creator',
          'description', 'date', 'time', 'attendees',
          'joined')
        depth = 1
         
class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['type', 'creator',
          'description', 'date', 'time']