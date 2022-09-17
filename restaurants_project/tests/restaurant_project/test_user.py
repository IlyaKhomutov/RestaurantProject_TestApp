import pytest


@pytest.mark.django_db
def test_admin_functions(client_admin, media_cleaning):
    """ALL ADMIN FUNCTIONS"""

    register_response = client_admin.post("/api/registration/",
                                          dict(first_name='Ivan', last_name='Ivanov', email='ivan@me.com',
                                               username='Ivan123',
                                               password='ivan456'))  # User registration

    creating_restaurant_response = client_admin.post("/api/restaurant/add/", dict(name='McDonalds',
                                                        address='Kiltseva Road, 1, Kiev, 02000'))  # Creating restaurant

    id_rest = creating_restaurant_response.data['id']  # ID of created restaurant

    updating_restaurant_response = client_admin.put(f"/api/restaurant/{id_rest}/update/", dict(name='McDonalds',
                                                  address='Independence Square, 1, Kiev, 02000'))  # Updating restaurant

    with open('test_image.png', 'rb') as fp:
        creating_menu_response = client_admin.post('/api/adding_menu/',
                                                   {'restaurant': id_rest,
                                                    'image': fp})  # Creating menu for the restaurant

    assert register_response.status_code == 200
    assert creating_restaurant_response.status_code == 201
    assert updating_restaurant_response.status_code == 200
    assert creating_menu_response.status_code == 201


@pytest.mark.django_db
def test_user_voting(data_for_user, client_user, media_cleaning):
    """VOTING"""

    vote_response = client_user.post("/api/vote/", dict(restaurant=data_for_user))
    assert vote_response.status_code == 201


@pytest.mark.django_db
def test_list_restaurants(data_for_user, client_user, media_cleaning):
    """LIST OF ALL RESTAURANTS AND THEIR MENUS"""

    restaurants_response = client_user.get("/api/restaurants/")
    assert restaurants_response.status_code == 200


@pytest.mark.django_db
def test_profile(data_for_user, client_user, media_cleaning):
    """USER PROFILE"""

    profile_response = client_user.get("/api/profile/")
    assert profile_response.status_code == 200


@pytest.mark.django_db
def test_voting_result(data_for_user, client_user, media_cleaning):
    """RESULT OF VOTING"""

    client_user.post("/api/vote/", dict(restaurant=data_for_user))
    vote_res_response = client_user.get("/api/result/")
    assert vote_res_response.status_code == 200
    print(vote_res_response.data)


@pytest.mark.django_db
def test_menu(data_for_user, client_user, media_cleaning):
    """ALL TODAY'S MENUS"""

    menus_response = client_user.get("/api/menus/")
    assert menus_response.status_code == 200


@pytest.mark.django_db
def test_menu_spec(data_for_user, client_user, media_cleaning):
    """TODAY'S MENUS OF SPECIFIC RESTAURANT"""

    spec_menu_response = client_user.get(f"/api/restaurant/{data_for_user}/menus/")
    assert spec_menu_response.status_code == 200
