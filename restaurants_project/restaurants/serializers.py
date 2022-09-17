from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'address',
        ]

    def validate(self, data):
        if Restaurant.objects.filter(name=data['name'], address=data['address']).exists():
            raise serializers.ValidationError("This restaurant is already exists")
        return data

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            'id',
            'date',
            'image'
        ]


class TodayMenusSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Menu
        fields = [
            'id',
            'restaurant',
            'image'
        ]


class MenuAddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            'restaurant',
            'date',
            'image'
        ]


class RestaurantRetrieveSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'address',
            'menus',
        ]
