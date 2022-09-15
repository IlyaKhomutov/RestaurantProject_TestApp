import datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Restaurant, Menu
from .serializers import RestaurantRetrieveSerializer, RestaurantAddSerializer, MenuAddingSerializer, \
    TodayMenusSerializer
from rest_framework import generics


class AddingRestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantAddSerializer
    permission_classes = (IsAdminUser,)


class UpdatingRestaurantView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = RestaurantAddSerializer
    lookup_field = 'id'


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    lookup_field = "id"
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantRetrieveSerializer


class AddingMenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = MenuAddingSerializer
    lookup_field = 'id'


class TodayMenusViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodayMenusSerializer
    lookup_field = 'id'

    def get_queryset(self):
        today = datetime.date.today()
        queryset = Menu.objects.filter(date=today)
        return queryset


class TodayRestaurantMenusViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodayMenusSerializer
    lookup_field = 'id'

    def get_queryset(self):
        today = datetime.date.today()
        queryset = Menu.objects.filter(date=today)
        request_id = self.kwargs['id']
        if request_id is not None:
            queryset = queryset.filter(restaurant_id=request_id)
        return queryset
