# Webbroad API Exemple

## Data Schema (Download .sql  [Link](https://drive.google.com/file/d/1_vStww4XH9TFJxzJxdrBzEE1l4HRGhCu/view?usp=sharing))



- **User**

| Name  |  Data Type | Description  |
| ------------ | ------------ | ------------ |
| **user_id**  | INT(11)  |  PK,NN,AI |
| email  |  VARCHAR(64) | NN,UQ  |
| password  | VARCHAR(32)  |NN   |
|username   | VARCHAR(32)  | NN,UQ  |
|first_name   | VARCHAR(64)  | NN  |
|last_name  |  VARCHAR(64)  | NN  |
| status | INT(11)  | default = 1   |

> **status : 0 = user  banned , 1 = user is not  verify email  , 2 = normal user

- **Post**

| Name  |  Data Type | Description  |
| ------------ | ------------ | ------------ |
| **post_id**  | INT(11)  |  PK,NN,AI |
| user_id  | INT(11)  |  NN |
| title  |  VARCHAR(128) | NN  |
| content  | VARCHAR(63206)  |NN   |
|time_stamp   | INT(11)  | NN  |

> **time_stamp use Unix Time

- **Comment**

| Name  |  Data Type | Description  |
| ------------ | ------------ | ------------ |
| **comment_id**  | INT(11)  |  PK,NN,AI |
| post_id  | INT(11)  |  PK,NN,AI |
| user_id  | INT(11)  |  NN |
| content  | VARCHAR(8000)  |NN   |
|time_stamp   | INT(11)  | NN,UQ  |

> **time_stamp use Unix Time

## API Document

- `POST /post/create`

##### Header requirement

| Key  |  Value |   
| ------------ | ------------ | 
|Authorization  | Basic base64endcode("email:password") | 
| Content-Type  | application/json|  

##### JSON Body

| Key  | Example  Value |   
| ------------ | ------------ | 
|title  | "Calculate"  | 
| content  | "10*10= ? "   

##### Example Requests.

```bash
curl --location --request POST 'http://127.0.0.1:8000/post/create' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk=' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Calculate#2",
    "content": "10*10=100"
}'
```


- `POST /post/comment/create`

##### Header requirement

| Key  |  Value |   
| ------------ | ------------ | 
|Authorization  | Basic base64endcode("email:password") | 
| Content-Type  | application/json|  

##### JSON Body

| Key  | Example  Value |   
| ------------ | ------------ | 
|post_id  | 1  | 
| content  | "10*10= 100"   

##### Example Requests.

```bash
curl --location --request POST 'http://127.0.0.1:8000/post/comment/create' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk=' \
--header 'Content-Type: application/json' \
--data-raw '{"post_id":1,"content":"4+1=100000"}'
```

- `POST /post/edit`

##### Header requirement

| Key  |  Value |   
| ------------ | ------------ | 
|Authorization  | Basic base64endcode("email:password") | 
| Content-Type  | application/json|  

##### JSON Body

| Key  | Example  Value |   
| ------------ | ------------ | 
|post_id  | 1  | 
| content  | "PigRabb 1+12 "  

##### Example Requests.

```bash
curl --location --request POST 'http://127.0.0.1:8000/post/edit' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk=' \
--header 'Content-Type: application/json' \
--data-raw '{"post_id" : 1 ,"content" : "PigRabb 1+12"}'
```

- `POST /post/comment/edit`

##### Header requirement

| Key  |  Value |   
| ------------ | ------------ | 
|Authorization  | Basic base64endcode("email:password") | 
| Content-Type  | application/json|  

##### JSON Body

| Key  | Example  Value |   
| ------------ | ------------ | 
|comment_id  | 1  | 
| content  | "PigRabb 1+12"  

##### Example Requests.

```bash
curl --location --request POST 'http://127.0.0.1:8000/post/comment/edit' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk=' \
--header 'Content-Type: application/json' \
--data-raw '{"comment_id" : 1 ,"content" : "PigRabb 1+12"}'
```

- `GET /post/show/post_id`

##### Header requirement

| Key  |  Value |   
| ------------ | ------------ | 
|Authorization  | Basic base64endcode("email:password") | 


##### Params

| Key  | Example  Value |   Description |
| ------------ | ------------ |  ------------ |
|id  | 1  |  post_id

##### Example Requests.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/show/post_id?id=2' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```

- `GET /post/show/user_id`

##### Header requirement

| Key  |  Value |   
| ------------ | ------------ | 
|Authorization  | Basic base64endcode("email:password") | 


##### Params

| Key  | Example  Value |   Description |
| ------------ | ------------ |  ------------ |
|**id**  | 1  |  user_id |
|limit  | 50  |  total result ; Max = 100 |
|start  | 2  |  start index |
|end  | 22  |  end index |

> end - start <= 100


##### Example Requests.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/show/user_id?id=1' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```
##### Example Requests with limit.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/show/user_id?id=1&limit=20' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```

##### Example Requests with start and end.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/show/user_id?id=1&start=2&end=10' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```


- `GET /post/show/all`

##### Header requirement

| Key  |  Value |   
| ------------ | ------------ | 
|Authorization  | Basic base64endcode("email:password") | 


##### Params

| Key  | Example  Value |   Description |
| ------------ | ------------ |  ------------ |
|limit  | 50  |  total result ; Max = 100 |
|start  | 2  |  start index |
|end  | 22  |  end index |

> end - start <= 100


##### Example Requests.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/show/all' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```
##### Example Requests with limit.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/show/all?limit=20' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```

##### Example Requests with start and end.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/show/all?start=100&end=1200' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```

- `GET /post/comment/show`

##### Header requirement

| Key  |  Value |   
| ------------ | ------------ | 
|Authorization  | Basic base64endcode("email:password") | 


##### Params

| Key  | Example  Value |   Description |
| ------------ | ------------ |  ------------ |
|id  | 1  |  post_id

##### Example Requests.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/comment/show?id=2' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```
##### Example Requests with limit.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/comment/show?id=2&limit=50' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```

##### Example Requests with start and end.

```bash
curl --location --request GET 'http://127.0.0.1:8000/post/comment/show?id=2&start=10&end=20' \
--header 'Authorization: Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk='
```




