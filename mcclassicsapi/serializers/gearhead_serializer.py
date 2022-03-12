from rest_framework import serializers
from mcclassicsapi.models import GearHead


class GearHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearHead
        fields = ('id','bio', 'profile_img', 'user')
        depth = 1
