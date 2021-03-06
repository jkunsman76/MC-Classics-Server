from rest_framework import serializers
from mcclassicsapi.models import Projects



class ProjectSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Projects
        fields = ('id','title', 'start_date', 'image', 'details', 'make',
                  'model', 'year', 'gear_head')
        depth = 2


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'start_date', 'details', 'make',
                    'model', 'year')