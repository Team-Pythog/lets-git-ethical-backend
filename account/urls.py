from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi
from django.contrib.auth import views as auth_views
from account import views as user_views
from .views import ShowProfilePageView

urlpatterns = [
      path('api/register', RegisterApi.as_view()),
      # path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
      
      path('<pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page')

      # path('edit-profile/', user_views.edit_profile, name='my_profile'),
      # path('my-profile', user_views.my_profile, name='my_profile')
]