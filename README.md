# REQUIREMENTS:
1. Only Back End (no needs to add UI); 
2. REST architecture; 
3. Tech stack: Django + DRF, JWT, PostgreSQL, Docker(docker-compose), PyTests; 
4. Added at least a few different tests; 
5. README.md with a description of how to run the system; 
6. Will be a + to add flake8 or smth similar

# TASK:
A company needs internal service for its employees which helps them to
make a decision at the lunch place. Each restaurant will be uploading menus
using the system every day over API.
Employees will vote for the menu before leaving for lunch on a mobile app
for whom the backend has to be implemented. There are users who did not
update the app to the latest version and the backend has to support both
versions. The mobile app always sends the build version in headers

# Functionality:
1. Authentication 
2. Creating restaurant 
3. Uploading menu for restaurant (There should be a menu for each day)
4. Creating employee 
5. Getting current day menu 
6. Getting results for the current day

#   How to run the system:
1. Clone code
2. Go to application root folder: "RestaurantProject_TestApp/restaurants_project"
3. Create .env file with your Django secret key
4. Run "sudo docker-compose up"

# Unauthorized users can: 
- Register: ("registraion/")
- Get their token: ("token/")

# Regular users(employees) can:
- Check their profile: ("/api/profile/")
- Check all restaurant and their menus for all days: ("/api/restaurants/")
- Check today's menus of a specific restaurant: ("/api/restaurant/<uuid:id>/menus/")
- Check all today's menus: ("/api/menus/")
- Vote: ("api/vote/")
- Check results of the today's vote: ("/api/result/")

# Users with Admin privileges can:
(All following methods work only with the "Bearer &lt;your access token&gt;", which must be in the header "Authorization")
- Create restaurant: ("/api/restaurant/add/")
- Update restaurant: ("/api/restaurant/<uuid:id>/update/")
- Add menu for any restaurant: ("/api/adding_menu/")

# How to run tests:
1. Create local virtual enviroment
2. Run "pip install -r requirements.txt"
3. Go to the folder with tests <tests/restaurant_project>
4. Run them using command "pytest" or directly from "test_user.py"
