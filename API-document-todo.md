
## get todo data
#### Request
- Method: **GET**
- URL:  ```/list/<account>```
   
- Headers：
    ```Content-Type: application/json```

#### Response
```
[
  {
    "todo_title": "3333",
    "todo_createtime": "2017:06:22",
    "todo_isFinsh": 0
  }
  ,
  {
    "todo_title": "2222",
    "todo_createtime": "2017:06:21",
    "todo_isFinsh": 0
  }
]
```

## create new todo
#### Request
- Method: **POST**
- URL:  ```/device/newdata```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "account":"swshawnwu@gmail.com",
  "todo_title": "reminder messages",
  "todo_createtime": "2017/08/06"
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

## finish todo
#### Request
- Method: **PATCH**
- URL:  ```/finish```
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "account":"swshawnwu@gmail.com",
  "todo_title": "reminder messages",
  "todo_createtime": "2017/08/06",
  "todo_isFinsh": 1
}
```
#### Response
```
True
```

## update todo content
#### Request
- Method: **PUT**
- URL:  ```/content```
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
	"account":"swshawnwu@gmail.com",
	"new_todo_title":"9876",
  "old_todo_title":"3333",
  "new_todo_createtime":"2017:05:13"
}
```
#### Response
```
True
```





## delete todo
#### Request
- Method: **DELETE**
- URL:  ```/<account>/<todo_title>```
   
- Headers：
    ```Content-Type: application/json```

#### Response
```
True
```
