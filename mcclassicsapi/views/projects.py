from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from mcclassicsapi.serializers import ProjectSerializer, CreateProjectSerializer
from mcclassicsapi.models import Projects, GearHead


class ProjectsView(ViewSet):
    """MC classics Projects view"""
    def list(self,request):
        """list all projects"""
        projects= Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def retrive(self,request, pk):
        """retrive requested project"""
        try:
            project= Projects.objects.get(pk=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Projects.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        """create new project"""
        gear_head = GearHead.objects.get(user=request.auth.user)
        try:
            serializer = CreateProjectSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(gear_head=gear_head)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk):
        """update projects"""
        project = Projects.objects.get(pk=pk)
        project.title = request.data["title"]
        project.make = request.data["make"]
        project.model = request.data["model"]
        project.year = request.data["year"]
        project.image = request.data["image"]
        project.details = request.data["details"]
        project.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk):
        """delete project"""
        project = Projects.objects.get(pk=pk)
        project.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)