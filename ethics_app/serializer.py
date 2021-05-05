from rest_framework import serializers
from .models import Dilemmas

class DilemmaSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('title', 'image', 'dilemma')
    model = Dilemmas