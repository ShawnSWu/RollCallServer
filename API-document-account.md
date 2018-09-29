# API
 https://{hostname}/account
 The hostname depends on Heroku

## sign up
#### Request
- Method: **POST**
- URL:  ```/signup```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "account":"swshawnwu@gmail.com",
  "password": "shawnpassword",
  "name": "shawn",
  "profile_image":"https://i.imgur.com/acuMhGW.jpg"
}
```

#### Response
```
Signup Success
```
or 
```
repeat account
```
