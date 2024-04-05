# Seal Mini Project 4
- **Backend**

- **By: Jason Kulak**
- **Name: Build-A-Burger**
- **Description: I am building a full CRUD application that will allow people to keep track of their favorite burgers.  This can be a burger you've made at home or one that you found at a restaurant.  The Index page will show a list of unique burgers names that the user can click on to get a more in depth description of that burger.  Once they click on said burger, the user will be taken to that burgers Show page giving a full description of the burger plus where it can be found.  User will be able to update/add ingredients, pictures, and location of where said burger can be found. There will also be an about section of the dev (me)**

- **Github URL: https://github.com/JasonKulak/Burger-Backend**

**Mini-Project4**
    - **Deployed Website: https://burger-backend-tq53.onrender.com/**

## Dependencies -
- asgiref
- dj-database-url
- Django
- django-cors-headers
- django-environ
- djangorestframework
- gunicorn
- packaging
- psycopg2-binary
- sqlparse
- typing_extensions

## Route Map
| Route Name  | Endpoint | Method | Description                 |
| ----------- | -------- | ------ | --------------------------- |
| Index |  /   | GET    | Renders all burgers on a page |
| Show | /:id | GET | Renders an individual burger |
| Create |  /   | POST    | Renders a created burger on the Index Page |
| Update | /:id   | PUT    | Updates data to a burger on the burger Index by id |
| Delete | /:id   | DELETE   | Removes a burger from the data array |


## ERD (Entity Relationship Diagram)
![Schema](https://imgur.com/lWKcfPA.jpg)


