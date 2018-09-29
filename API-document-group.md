# API
__***https://{hostname}/account***__ <br>
 The hostname depends on Heroku


## get group data
#### Request
- Method: **GET**
- URL:  ```/device/list/<account>/<group_name>```
   
- Headers：
    ```Content-Type: application/json```

#### Response
```
{
 "RollCall_07": "C7:46:BC:63:26:05", 
 "RollCall_08": "C6:46:BC:D8:24:05", 
 "RollCall_09": "C5:46:B1:D3:25:05",
 "RollCall_10": "C4:46:B5:D3:29:05"
}
```



## insert new data to List
#### Request
- Method: **POST**
- URL:  ```/device/newdata```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "insert_type": "extra_add"
  "account":"swshawnwu@gmail.com",
  "list_name": "LondonEngland",
  "list_key": "C4:46:B5:D3:29:05",
  "list_value": "RollCall_10",
  "group_image_uri": "https://i.imgur.com/A4p9Tix.jpg",

}
```
| insert_type | Meaning |
| ------| ------ | 
| add_new | add a few new data | 
| extra_add | won't delete earlier data | 

#### Response
```
True
```
or 
```
False
```




## get all group data
#### Request
- Method: **GET**
- URL:  ```/info/<account>```
   
- Headers：
    ```Content-Type: application/json```
- Body:

#### Response
```
[
  {"listname": "America",
   "people_count": 14,
   "group_image_uri": "https://i.imgur.com/F4cwNJT.jpg"
  }
]
```

## create group
#### Request
- Method: **POST**
- URL:  ```/create```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "account":"swshawnwu@gmail.com",
  "listname": "LondonEngland",
  "group_image_uri": "https://i.imgur.com/A4p9Tix.jpg"

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

## delete group
#### Request
- Method: **DELETE**
- URL:  ```/delete/<account>/<group_name>```
   
- Headers：
    ```Content-Type: application/json```

#### Response
```
True
```
or 
```
False
```

## get group count
#### Request
- Method: **GET**
- URL:  ```/device/list/<account>/<group_name>```
   
- Headers：
    ```Content-Type: application/json```

#### Response
```
{
  9
}
```

## get all list name
#### Request
- Method: **GET**
- URL:  ```/name/<account>```
   
- Headers：
    ```Content-Type: application/json```

#### Response
```
{
  ["America", "Japan", "LondonEngland"]
}
```


## get some group list data
#### Request
- Method: **GET**
- URL:  ```/info/<account>/<group_name>```
   
- Headers：
    ```Content-Type: application/json```

#### Response
```
{
  {"people_count": 9, "group_image_uri": "https://i.imgur.com/A4p9Tix.jpg"}
}
```
