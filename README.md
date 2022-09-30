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

