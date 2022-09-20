from django.urls import path
from .views import RestaurantViewSet, AddingRestaurantViewSet, UpdatingRestaurantView, AddingMenuViewSet, \
    TodayMenusViewSet

urlpatterns = [
    path('restaurants/', RestaurantViewSet.as_view({'get': 'list'}), name='restaurant_list'),
    path('restaurant/add/', AddingRestaurantViewSet.as_view({'post': 'create'}, ), name='restaurant_adding'),
    path('restaurant/<uuid:id>/update/', UpdatingRestaurantView.as_view(), name='restaurant_updating'),
    path('adding_menu/', AddingMenuViewSet.as_view({'post': 'create'}), name='menu_adding'),
    path('menus/', TodayMenusViewSet.as_view({'get': 'list'}), name='all_todays_menus'),
]
