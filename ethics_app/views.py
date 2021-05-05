from django.shortcuts import render
from rest_framework import generics
from .serializer import DilemmaSerializer
from .models import Dilemmas

class DilemmaList(generics.ListCreateAPIView): # displays in JSOn format
  queryset = Dilemmas.objects.all()
  serializer_class = DilemmaSerializer

class DilemmaDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Dilemmas.objects.all()
  serializer_class = DilemmaSerializer