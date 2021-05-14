from rest_framework import generics, permissions
from .models import Dilemmas
from .serializer import DilemmaSerializer


class DilemmaList(generics.ListCreateAPIView):
    # permission_classes = (permissions.AllowAny,)
    queryset = Dilemmas.objects.all()
    serializer_class = DilemmaSerializer

class DilemmaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dilemmas.objects.all()
    serializer_class = DilemmaSerializer