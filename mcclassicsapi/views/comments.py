from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from mcclassicsapi.models import Comments, GearHead, Projects
from mcclassicsapi.serializers import (CommentsSerializer, CreateCommentSerializer)


class CommentsView(ViewSet):
    """MC classics Comments view"""
    # match pk that comes from url
    def retrieve(self, request, pk):
        """retrive selected comments"""
        author = GearHead.objects.get(user=request.auth.user)
        try:
            comment = Comments.objects.get(pk=pk)
            if comment.author == author:
                comment.is_owner = True
            else:
                comment.is_owner = False
            serializer = CommentsSerializer(comment)
            return Response(serializer.data)
        except Comments.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """retrive all comments"""
        comments = Comments.objects.all()
        author = GearHead.objects.get(user=request.auth.user)
        for comment in comments:
            if comment.author == author:
                comment.is_owner = True
            else:
                comment.is_owner = False

        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ create new comment"""
        project = Projects.objects.get(pk=request.data['project'])
        gearhead = GearHead.objects.get(user_id=request.auth.user_id)
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=gearhead, project=project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Update comment"""
        comment = Comments.objects.get(pk=pk)
        comment.content = request.data['content']
        comment.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """bye bye comment"""
        comment = Comments.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    

    