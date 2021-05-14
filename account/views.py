from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Profile
from django.views import generic
from .serializer import ProfileSerializer
from django.views.generic import DetailView
from rest_framework import generics


class ShowProfilePageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    model = Profile
    
    def get_profile_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        # page_user = get_object_or_404(users, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class EditProfilePageView(generic.CreateView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    model = Profile

    def get_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        if self.method == 'POST':
            form = ProfileUpdateForm(self.POST, instance=self.user)
            if form.is_valid():
                form.save()
        else: 
            form = ProfileUpdateForm()
        context['form'] = form
        return context