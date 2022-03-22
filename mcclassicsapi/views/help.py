from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from mcclassicsapi.models import Help, GearHead, Projects
from mcclassicsapi.serializers import HelpSerializer, CreateHelpSerializer

class HelpView(ViewSet):
    """MC classics Help view"""
    #  match pk that comes from url
    def retrieve(self, request, pk):
        """retrive selected help"""
        author = GearHead.objects.get(user=request.auth.user)
        try:
            hlp = Help.objects.get(pk=pk)
            if hlp.author == author:
                hlp.is_owner = True
            else:
                hlp.is_owner = False
            serializer = HelpSerializer(hlp)
            return Response(serializer.data)
        except Help.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """retrive all help"""
        hlp = Help.objects.all()
        author = GearHead.objects.get(user=request.auth.user)
        for hp in hlp:
            if hp.author == author:
                hp.is_owner = True
            else:
                hp.is_owner = False

        serializer = HelpSerializer(hlp, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ create new help"""
        project = Projects.objects.get(pk=request.data['project'])
        gearhead = GearHead.objects.get(user_id=request.auth.user_id)

        serializer = CreateHelpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=gearhead, project=project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Update help"""
        hlp = Help.objects.get(pk=pk)
        hlp.content = request.data['content']
        hlp.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """bye bye help"""
        hlp = Help.objects.get(pk=pk)
        hlp.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    @action(methods=['get'], detail=False)
    def usersrequests(self, request):
        """Gets the current user at http://localhost:8000/help/usersrequests"""
        gear_head= GearHead.objects.get(user=request.auth.user)
        requests = Help.objects.filter(gear_head_id=gear_head.id)
        serializer = HelpSerializer(requests, many=True)
        return Response(serializer.data)