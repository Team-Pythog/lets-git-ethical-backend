from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import DilemmaSerializer, UserSerializer, UserSerializerWithToken
from .models import Dilemmas

#this view will be used each time a user revists the site (e.g. page reload, anything that causes state change)
@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    # Note: permission_classes variable allows users to sign up without being logged in first -- that would be a bug!
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('test')


class DilemmaList(generics.ListCreateAPIView):
    queryset = Dilemmas.objects.all()
    serializer_class = DilemmaSerializer

class DilemmaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dilemmas.objects.all()
    serializer_class = DilemmaSerializer

# class ProfileInfoList(generics.ListAPIView):
#     queryset = ProfileInfo.objects.all()
#     serializer_class = ProfileInfoSerializer

# class ProfileInfoDelete(generics.RetrieveDestroyAPIView):
#     queryset = ProfileInfo.objects.all()
#     serializer_class = ProfileInfoSerializer