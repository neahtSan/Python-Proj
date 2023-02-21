
# myDropbox_6570108321 (Activity 6)

A brief description of what this project does and who it's for




## Authors

- [@Tanisa124](https://github.com/Tanisa124) (Mr. Thaenthai Opathum)




## Used By

This project is used by studying purpose only:

- Cloud Computing 2110524



## API Reference

#### Write login user file access in dynamodb table
```
    POST /api/Activity-6-user
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `image`      | `string` | **Required**. file that user have access to |
| `format_date`      | `string` | **Required**. cuurent datetime |
| `size`      | `string` | **Required**. size of the file |

#### View login user file access in dynamodb table
```
    POST /api/Activity-6-user
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `all_images`      | `string` | **Required**. All file in AWS S3 bucket |

#### Get AWS S3 All file
```
    GET /api/Activity-5-Lambda
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `none`      | `string` | - |



#### Get all file name in AWS S3 that login user have access to

```http
  GET /api/Activity-5-Lambda
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |

#### Get file from AWS S3 (download) that login user have access to

```http
  POST /api/Activity-5-download
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileName`      | `string` | **Required**. name of download file |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `owner`      | `string` | **Required**. owner of the selected file |


#### Put file to AWS S3 (upload) and write access for login user in dynamodb

```http
  POST /api/Activity-5-upload
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileName`      | `string` | **Required**. name of upload file |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |



#### download file 

will be downloaded to `sourceCode directory` inside work project

#### upload file

need to be in `sourceCode directory` inside work project before upload

#### Create newuser in dynamodb table if user not exist

```http
  POST /api/Activity-6-user
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |

#### login the user if user exist and correct password

```http
  POST /api/Activity-6-user
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `login_state` | `bool` | **Required**. show that user currently login or not

#### Share a file to exist user in dynamodb table if user is a owner 

```http
  POST /api/Activity-6-user
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `image`      | `string` | **Required**. file name |
| `shared_user`      | `string` | **Required**. user that want to share a file to |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |





## Directories tree

* **sourceCode/**
    * `myDropbox_client_6570108321.py`
    * `download file`
    * `upload file`
    * **components/**
        * `check.py`
        * `logic.py`
        * `message.py`
        * `myPath.py`
        * `user.py`


## Functionality

* **myDropbox.py (main)**
    * run this script to use the application

* **components/check.py**
    * `check command` from user
    * `check file` in upload directory
    * `check logout` need to login first
    * `check download` correct owner name or not

* **components/message.py**
    * `send message` to user when run the application for the first time
    * `send list of command` user can use when accepted help command 

* **components/mypath.py**
    * return `sorceCode directory` path for upload and download
    * return all file in `sorceCode directory`

* **components/logic.py**
    * return `all file name, modifiedDate, size, and owner` that login user have access to in AWS S3
    * `download file` from AWS S3 to `sorceCode directory` that login user have access to and given correct owner name
    * `upload file` to AWS S3 from `sorceCode directory` and write user access in dynamodb table
    * `create newuser` if user have not register yet and write it in dynamodb table
    * `login user` if user have already register and give the correct password
    * `share file` if shared user have alredy register, not have access to that file, and login user is the owner of that file



## API Request & Response

#### Write login user file access in dynamodb table
```http
    POST https://2ehzl1lfy6.execute-api.us-west-1.amazonaws.com/defaultActivity-6-user
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `image`      | `string` | **Required**. file that user have access to |
| `format_date`      | `string` | **Required**. cuurent datetime |
| `size`      | `string` | **Required**. size of the file |
| `endpoint` | `string` | `/Activity-6-user` |
| `headers` | `dict` | `'Content-Type': 'application/json'`|
|`payload` | `json` | `{user: user, password: password, image: image, format_date: format_date, size: size}` |

* Response Format

**for http status 200**

    'OK'

**for http status 401**

    'File: {filename} already existed'

#### View login user all file access in dynamodb table
```http
    POST https://2ehzl1lfy6.execute-api.us-west-1.amazonaws.com/defaultActivity-6-user
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `all_images`      | `string` | **Required**. All file in AWS S3 bucket |
| `endpoint` | `string` | `/Activity-6-user` |
| `headers` | `dict` | `'Content-Type': 'application/json'`|
|`payload` | `json` | `{user: user, password: password, all_images: all_images}` |

* Response Format

**for http status 200**

    '[{'image': {file_name}, 'lastModifiedDate': {lastModifiedDate}, 'size': {size}, 'owner': {owner}}, {...}, . . .]'

**for http status 401**

    'User: {user} have no access to any file'

#### Get AWS S3 All file
```http
    GET https://2ehzl1lfy6.execute-api.us-west-1.amazonaws.com/defaultActivity-5-Lambda
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `none`      | `none` | - |
| `endpoint` | `string` | `/Activity-5-Lambda` |
| `headers` | `dict` | `'Content-Type': 'application/json'`|
|`payload` | `json` | `{}` |

* Response Format

**for http status 200**

    [filename1, filename2, filename3, . . . ]

**for http status 401**

    []



#### Get file from AWS S3 (download) that login user have access to

* Request Format
```http
  POST https://2ehzl1lfy6.execute-api.us-west-1.amazonaws.com/default/Activity-5-download
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileName`      | `string` | **Required**. name of download file |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `owner`      | `string` | **Required**. owner of selected file |
| `endpoint` | `string` | `/Activity-5-download` |
| `headers` | `dict` | `'Content-Type': 'application/json'`|
|`payload` | `json` | `{fileName: fileName, user: user, password: password, owner: owner}` |

* Response Format

**for 'access grant'**

    download [fileName] at [../download directory] complete!

**for False**

    User: {user} cannot access to file: {fileName}

**for 'wrong owner name'**

    Wrong owner name: {owner}



#### Put file to AWS S3 (upload)

* Request Format
```http
  POST https://2ehzl1lfy6.execute-api.us-west-1.amazonaws.com/default/Activity-5-upload
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileName`      | `string` | **Required**. name of upload file |
| `endpoint` | `string` | `/Activity-5-upload` |
| `headers` | `dict` | `'Content-Type': 'application/json'`|
|`payload` | `json` | `{fileName: fileName, rawText: body}` |

* Response Format

**for http status 200**

    upload [fileName] to myDropbox success!

**for http status 400**

    Already have file name: [fileName] in myDropbox

#### Create newuser in dynamodb table if user not exist
```http
    POST https://2ehzl1lfy6.execute-api.us-west-1.amazonaws.com/defaultActivity-6-user
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `endpoint` | `string` | `/Activity-6-user` |
| `headers` | `dict` | `'Content-Type': 'application/json'`|
|`payload` | `json` | `{user: user, password: password}` |

* Response Format

**for http status 200**

    'OK'

**for http status 401**

    'User: {user} already existed!'

#### login the user if user exist and correct password
```http
    POST https://2ehzl1lfy6.execute-api.us-west-1.amazonaws.com/defaultActivity-6-user
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `login_state` | `bool` | **Required**. show that user currently login or not|
| `endpoint` | `string` | `/Activity-6-user` |
| `headers` | `dict` | `'Content-Type': 'application/json'`|
|`payload` | `json` | `{user: user, password: password}` |

* Response Format

**for http status 200**

    'OK'

**for http status 401**

Correct username but wrong password

    'Wrong password for user: {user}'

Wrong username

    'No username: {user}, Please create newuser'

#### Share a file to exist user in dynamodb table if user is a owner 
```http
    POST https://2ehzl1lfy6.execute-api.us-west-1.amazonaws.com/defaultActivity-6-user
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `image`      | `string` | **Required**. file name |
| `shared_user`      | `string` | **Required**. user that want to share a file to |
| `user`      | `string` | **Required**. username of login user |
| `password`      | `string` | **Required**. password of login user |
| `endpoint` | `string` | `/Activity-6-user` |
| `headers` | `dict` | `'Content-Type': 'application/json'`|
|`payload` | `json` | `{user: user, password: password, image: image, all_images, shared_user: shared_user}` |

* Response Format

**for http status 200**

    'OK'

**for http status 401**

shared user don't have an acoount

    'Cannot shared to this user, no account name: {shared_user}'

shared user already have access to the file

    'User: {shared_user} already have access to file: {image}'

user not the owner of the file

    'User: {user} not the owner of file: {file_name}'

