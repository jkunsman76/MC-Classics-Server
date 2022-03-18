from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


from mcclassicsapi.models import GearHead
from mcclassicsapi.serializers import GearHeadSerializer


class ProfileView(ViewSet):
    def list(self, request):
        """list all gearheads"""
        gear_heads = GearHead.objects.all()
        serializer = GearHeadSerializer(gear_heads, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def currentuser(self, request):
        """Gets the current user at http://localhost:8000/api/profiles/currentuser"""
        gear_head = GearHead.objects.get(user=request.auth.user)
        serializer = GearHeadSerializer(gear_head)
        return Response(serializer.data)
    