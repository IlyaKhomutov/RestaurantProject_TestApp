import datetime
from rest_framework import serializers, status
from .models import CustomUser
from restaurants.models import Vote


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=5)
    username = serializers.CharField(max_length=50, min_length=5)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'username',
            'password',
            'is_staff',
        ]

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': "email already exists"})
        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': "username already exists"})

        return super().validate(args)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class ResultSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Vote
        fields = [
            'id',
            'user',
            'restaurant'
        ]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = [
            'id',
            'restaurant',
            'date'
        ]

    def validate(self, data):
        request = self.context.get('request', None)
        user = request.user
        today = datetime.date.today()
        if Vote.objects.filter(user=user, date=today).exists():
            raise serializers.ValidationError("You have already voted today")
        return data

    def create(self, validated_data):
        return Vote.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class InnerVoteSerializer(serializers.ModelSerializer):
        restaurant = serializers.StringRelatedField()

        class Meta:
            model = Vote
            fields = [
                'id',
                'restaurant',
                'date'
            ]
    votes = InnerVoteSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'votes',
        ]
