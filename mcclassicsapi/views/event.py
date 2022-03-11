from django.core.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from mcclassicsapi.models import Event, GearHead
from mcclassicsapi.serializers import EventSerializer, CreateEventSerializer

class EventView(ViewSet):

    def retrieve(self, request, pk):
        """Retrive Event"""
        try:
            event= Event.objects.get(pk=pk)
            serializer= EventSerializer(event)
            return Response(serializer.data)
        except  Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """ list all events"""
        events=Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
       
    def create(self, request):
        """ create new event"""
        gear_head = GearHead.objects.get(user=request.auth.user)
        try:
            serializer = CreateEventSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(creator=gear_head)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
   
    def update(self, request, pk):
        """ update event"""
        try:
            event = Event.objects.get(pk=pk)
            serializer = CreateEventSerializer(event, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        """ delete event"""
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """ join event"""
        gear_head = GearHead.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.add(gear_head)
        return Response({'message': 'Gear_head added'}, status=status.HTTP_201_CREATED)
    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """leave event"""
        gear_head = GearHead.objects.get(user=request.auth.user)
        event= Event.objects.get(pk=pk)
        event.attendees.remove(gear_head)
        return Response({'message': 'Gear_head removed'}, status=status.HTTP_204_NO_CONTENT)
    