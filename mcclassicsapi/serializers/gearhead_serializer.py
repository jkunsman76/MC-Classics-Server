from rest_framework import serializers
from mcclassicsapi.serializers import UserSerializer
from mcclassicsapi.models import GearHead


class GearHeadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = GearHead
        fields = ('id','bio', 'profile_img', 'user')
        depth = 1
