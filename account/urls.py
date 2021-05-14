from .api import RegisterApi
from django.conf.urls import url
from django.urls import path, include
from account import views as user_views
from .views import ProfileListView, ProfileDetailView, current_user

urlpatterns = [
      path('register/', RegisterApi.as_view()),
      path('current_user/', current_user),
      path('profile/', ProfileListView.as_view(), name='profile_list'),
      path('profile/<str:username>', ProfileDetailView.as_view(), name='profile_details')
      # path('<int:pk>/profile/', ProfileListView.as_view(), name='show_profile_page'),
      # path('<int:pk>/profile/edit', EditProfilePageView.as_view(), name='edit_profile'),
      # path('edit-profile/', user_views.edit_profile, name='my_profile'),
      # path('my-profile', user_views.my_profile, name='my_profile')
]