from rest_framework import serializers
from .models import SpeedData

class SpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedData
        fields = "__all__"
