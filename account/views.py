from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile
from .serializer import UserSerializer, ProfileSerializer


#this view will be used each time a user revists the site (e.g. page reload, anything that causes state change)
@api_view(['GET', 'POST', 'PUT'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

# def get_profile_data(self, *args, **kwargs):
#     context = super(ProfileListView, self).get_context_data(*args, **kwargs) 
#     page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#     context['page_user'] = page_user
#     return context

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field='user__username'
    lookup_url_kwarg='username'

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field='user__username'
    lookup_url_kwarg='username'

# class EditProfilePageView(generic.CreateView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     model = Profile

#     def get_data(self, *args, **kwargs):
#         context = super(ProfileListView, self).get_context_data(*args, **kwargs)
#         if self.method == 'POST':
#             form = ProfileUpdateForm(self.POST, instance=self.user)
#             if form.is_valid():
#                 form.save()
#         else: 
#             form = ProfileUpdateForm()
#         context['form'] = form
#         return context