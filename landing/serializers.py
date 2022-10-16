from rest_framework import serializers
from landing.models import Landing




class LandingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Landing
        fields = "__all__"