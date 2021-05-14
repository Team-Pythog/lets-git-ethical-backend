from .models import Dilemmas
from rest_framework import serializers

class DilemmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dilemmas
        fields = ('id', 'title', 'image', 'text', 'response_0', 'response_1')