from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from mcclassicsapi.models import GearHead
from mcclassicsapi.serializers import GearHeadSerializer, UserSerializer


class ProfileView(ViewSet):
    def list(self, request):
        """list all gearheads"""
        gear_heads = GearHead.objects.all()
        serializer = GearHeadSerializer(gear_heads, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def currentuser(self, request):
        """Gets the current user at http://localhost:8000/profiles/currentuser"""
        gear_head = GearHead.objects.get(user=request.auth.user)
        serializer = GearHeadSerializer(gear_head)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """update gear_head and user data"""
        try:
            gear_head = GearHead.objects.get(pk=pk)
            gear_head.bio = request.data['bio']
            user = request.auth.user
            user.username=request.data['username']
            user.first_name=request.data['first_name']
            user.last_name=request.data['last_name']
            user.email=request.data['email']
            gear_head.save()
            user.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        """bye bye gear_head"""
        gear_head = GearHead.objects.get(pk=pk)
        user = User.objects.get(id=request.auth.user.id)
        gear_head.delete()
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    