from django.urls import path
from .views import DilemmaList, DilemmaDetail

urlpatterns = [
  path('', DilemmaList.as_view(), name='dilemma_list'),
  path('<int:pk>', DilemmaDetail.as_view(), name='dilemma_detail')
]