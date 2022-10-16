from rest_framework import serializers
from football.models import Landing




class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Landing
        fields = '__all__'