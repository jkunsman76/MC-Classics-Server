from rest_framework import serializers
from mcclassicsapi.models import Comments



class CommentsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Comments
        fields = ('id', 'content', 'project', 'author')
        depth = 2


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('content', 'project_id')