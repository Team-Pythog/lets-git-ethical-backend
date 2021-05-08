from django.urls import path
from .views import DilemmaList, DilemmaDetail, ProfileInfoList
from .views import current_user, UserList

urlpatterns = [
  path('', DilemmaList.as_view(), name='dilemma_list'),
  path('<int:pk>', DilemmaDetail.as_view(), name='dilemma_detail'),
  path('users/', UserList.as_view()),
  path('current_user/', current_user),
  path('profiles/', ProfileInfoList.as_view(), name='profile_list')
]