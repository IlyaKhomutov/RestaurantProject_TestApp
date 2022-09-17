from django.urls import path
from .views import RegistrationAPIView, ResultViewSet, VoteViewSet, ProfileViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('result/', ResultViewSet.as_view({'get': 'list'}), name='result'),
    path('profile/', ProfileViewSet.as_view({'get': 'retrieve'}), name='profile'),
    path('vote/', VoteViewSet.as_view({'post': 'create'}), name='voting'),
]
