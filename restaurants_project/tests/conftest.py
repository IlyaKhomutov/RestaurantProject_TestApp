import pytest
from rest_framework.test import APIClient
from accounts.models import CustomUser
import os
from restaurants_project import settings

client = APIClient()


@pytest.fixture
def client_admin():
    """CLIENT FOR ADMIN"""
    admin = CustomUser.objects.create_user(first_name='admin', last_name='admin', email='admin@pro.com',
                                           username='admin',
                                           password='admin', is_staff=True)
    admin_token_response = client.post("/api/token/",
                                       dict(username='admin', password='admin'))  # Getting admin token
    admin_token = admin_token_response.data['access']  # Admin token
    client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(admin_token))  # Adding admin token to headers
    return client


@pytest.fixture
def client_user():
    """CLIENT FOR USER"""
    user_token_response = client.post("/api/token/",
                                      dict(username='Ivan123', password='ivan456'))  # Getting user token
    user_token = user_token_response.data['access']  # user token
    client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(user_token))  # Adding admin token to headers
    return client


@pytest.fixture
def data_for_user():
    CustomUser.objects.create_user(first_name='admin', last_name='admin', email='admin@pro.com',
                                   username='admin',
                                   password='admin', is_staff=True)

    admin_token_response = client.post("/api/token/",
                                       dict(username='admin', password='admin'))  # Getting admin token
    admin_token = admin_token_response.data['access']  # Admin token

    client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(admin_token))  # Adding admin token to headers

    client.post("/api/registration/",
                dict(first_name='Ivan', last_name='Ivanov', email='ivan@me.com', username='Ivan123',
                     password='ivan456'))  # User registration

    creating_restaurant_response = client.post("/api/restaurant/add/", dict(name='McDonalds',
                                                        address='Kiltseva Road, 1, Kiev, 02000'))  # Creating restaurant

    id_rest = creating_restaurant_response.data['id']  # ID of created restaurant

    client.put(f"/api/restaurant/{id_rest}/update/",
               dict(name='McDonalds', address='Independence Square, 1, Kiev, 02000'))  # Updating restaurant

    with open('test_image.png', 'rb') as fp:
        client.post('/api/adding_menu/', {'restaurant': id_rest, 'image': fp})  # Creating menu for the restaurant

    return id_rest


@pytest.fixture
def media_cleaning():
    """FUNCTION FOR CLEANING MEDIA FILES AFTER TESTS"""
    for months, days, images in os.walk(settings.MEDIA_ROOT + settings.MEDIA_URL + "files/"):
        for image in images:
            if str(image).startswith("test_image"):
                os.remove(months + "/" + image)
            if len(os.listdir(months)) == 0:
                os.rmdir(months)


