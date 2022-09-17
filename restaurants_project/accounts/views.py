import datetime
from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ResultSerializer, VoteSerializer, RegistrationSerializer, UserSerializer
from rest_framework import generics
from restaurants.models import Vote


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class ResultViewSet(viewsets.ModelViewSet):
    today = datetime.date.today()
    queryset = Vote.objects.filter(date=today)
    serializer_class = ResultSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_object(self):
        return self.request.user


class VoteViewSet(viewsets.ModelViewSet):
    today = datetime.date.today()
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    lookup_field = "id"
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
