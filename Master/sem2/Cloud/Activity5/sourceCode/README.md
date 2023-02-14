
# myDropbox_6570108321 (Activity 5)

A brief description of what this project does and who it's for




## Authors

- [@Tanisa124](https://github.com/Tanisa124) (Mr. Thaenthai Opathum)




## Used By

This project is used by studying purpose only:

- Cloud Computing 2110524



## API Reference

#### Get all file name in AWS S3 

```http
  GET /api/Activity-5-Lambda
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `none` | `-` | `-` |

#### Get file from AWS S3 (download)

```http
  POST /api/Activity-5-download
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileName`      | `string` | **Required**. name of download file |

#### Put file to AWS S3 (upload)

```http
  POST /api/Activity-5-upload
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fileName`      | `string` | **Required**. name of upload file |



#### download file 

will be downloaded to `download directory` inside work project

#### upload file

need to be in `upload directory` inside work project before upload




## Directories tree

* **sourceCode/**
    * `myDropbox.py`
    * **components/**
        * `check.py`
        * `logic.py`
        * `message.py`
        * `myPath.py`
    * **download/**
    * **upload/**

## Functionality

* **myDropbox.py (main)**
    * run this script to use the application

* **components/check.py**
    * `check command` from user
    * `check file` in upload directory

* **components/message.py**
    * `send message` to user when run the application for the first time
    * `send list of command` user can use when accepted help command 

* **components/mypath.py**
    * return `download directory` or create it
    * return `upload directory` or create it
    * return all file in `upload directory`

* **components/logic.py**
    * return `all file name` in AWS S3
    * `download file` from AWS S3 to `download directory`
    * `upload file` to AWS S3 from `upload directory`


