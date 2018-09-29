# API
__***https://{hostname}/account***__ <br>
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


## log in
#### Request
- Method: **POST**
- URL:  ```/login```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "account":"swshawnwu@gmail.com",
  "password": "shawnpassword"
}
```

#### Response
```
True
```
or 
```
False
```


## get procfile data
#### Request
- Method: **GET**
- URL:  ```/profile/<account>```
   
- Headers：
    ```Content-Type: application/json```
- Body:

#### Response
```
{
  "account":"swshawnwu@gmail.com",
  "name": "shawn",
  "profile_image":"https://i.imgur.com/acuMhGW.jpg"
}
```


## get every number of group device
#### Request
- Method: **GET**
- URL:  ```/profile/deviceamount/<account>```
   
- Headers：
    ```Content-Type: application/json```
- Body:

#### Response
```
{
  [2, 1, 9]
}
```



## save profile image
#### Request
- Method: **POST**
- URL:  ```/profile/profile_image```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "account":"swshawnwu@gmail.com",
  "profile_image":"https://i.imgur.com/acuMhGW.jpg"
}
```

#### Response
```
success
```
