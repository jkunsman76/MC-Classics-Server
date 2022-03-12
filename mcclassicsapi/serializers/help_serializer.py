from rest_framework import serializers
from mcclassicsapi.models import Help


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('id', 'content', 'project', 'author')
        depth = 1


class CreateHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('content', 'project_id')