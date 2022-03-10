from rest_framework import serializers
from mcclassicsapi.models import GearHead


class GearHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearHead
        fields = ('bio', 'profile_image', 'user')
        depth = 1
