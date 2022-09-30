# coupon-management-flask
Flask API service to manage and use coupons for users.


## What it does
In this project we've created an coupon management service for users. Users in this project have a credit, which they can use to buy coupons. Using these coupons, they can get discounts, gifts, or whatever we may need in our projects. 
Each coupon has a certain value, a hidden code for using the coupon, and a certain number of times which it can be used. 
We have implemented the policy so  that in the following scenarios, the API returns proper responses to user:


1. One user wants to use a certain coupon more than once. 
2. The credit of user is less than the value of the coupon
3. The number of remaining coupons is zero. 
4. The hidden code entered by the user is wrong. 

Also to address the security issues, we use token based authentication for users. (We assume that some users are already in database) To login a user must provide correct username and password of which we've saved a hash string in database. If the provided information matches to one of the users, an access token and a refresh token are created and sent to the user. 
Access tokens have expiration dates, so when that happens, user must call another API and provide the refresh token as input, to receive another valid access token. (To be able to call each of the API endpoints, user must provide valid access token.)



## How to run
Running this project is very simple. Basically we use two services running inside docker containers. One is a PostgreSQL service for our database, and the other is our main api service. To run the project you need to setup the config for your system. First of all, you need to edit the docker-compose file, and enter your postgres username, password and db name. Also you config exposed ports for the DB and API service, and more importantly, your database volume. 
Secondly, you need to edit [**application.yml**](https://github.com/amirfaghihi/coupon-management-flask/blob/7c7a2f8ead9fb94795a572032813842aad6e34a7/coupon_management_flask/application.yml) file. This file basically tells the API service to connect to your database service. 
After doing the configuration, you only need to run the following command:


`docker-compose up -d --build`

This command builds DB and API images and creates their container. The sample postman collection is included inside the repository, so you can just change the IP address from urls and execute your APIs. 

**Notice: Inside the code we have a function called init_db in [_application.py_](https://github.com/amirfaghihi/coupon-management-flask/blob/7c7a2f8ead9fb94795a572032813842aad6e34a7/coupon_management_flask/coupon_management_flask/application.py). This function is used to add some initial user and coupon data to the database. You can run the project locally and execute this function to initialize your tables.**


## The stack we've used

* Flask Framework 
* SQLAlchemy orm 
* PostgreSQL database
* Docker & docker-compose for containerization
* Marshmallow for serialization and deserialization
