# IMDB-like-app
Sample of imdb application using flask and postgresql

## Overview

* Database: postgres
* Language: python 3
* Web Framework: flask



Sample Postman requests
```
import http.client

conn = http.client.HTTPConnection("localhost")

payload = "{\n    \"moviename\": \"Lucifer\",\n    \"releasedate\":\"2019-01-10\",\n    \"budget\": 25000000,\n    \"collection\": 500000000,\n    \"description\": \"illuminati\",\n    \"actors\":[\n        {\n            \"firstname\": \"Mohan\",\n            \"lastname\": \"Lal\",\n            \"dob\": \"1990-03-09\",\n            \"description\": \"stephen Nedumpalli\"\n        },\n        {\n            \"firstname\": \"Mohan\",\n            \"lastname\": \"Lal\",\n            \"dob\": \"1990-03-09\",\n            \"description\": \"stephen Nedumpalli\"\n        },\n        {\n            \"firstname\": \"Mohan\",\n            \"lastname\": \"Lal\",\n            \"dob\": \"1990-03-09\",\n            \"description\": \"stephen Nedumpalli\"\n        }\n    ],\n    \"producers\":[\n        {\n            \"firstname\": \"Mohan\",\n            \"lastname\": \"Lal\",\n            \"dob\": \"1990-03-09\",\n            \"description\": \"stephen Nedumpalli\"\n        },\n        {\n            \"firstname\": \"Mohan\",\n            \"lastname\": \"Lal\",\n            \"dob\": \"1990-03-09\",\n            \"description\": \"stephen Nedumpalli\"\n        },\n        {\n            \"firstname\": \"Mohan\",\n            \"lastname\": \"Lal\",\n            \"dob\": \"1990-03-09\",\n            \"description\": \"stephen Nedumpalli\"\n        }\n    ],\n    \"directors\":[\n        {\n            \"firstname\": \"Mohan\",\n            \"lastname\": \"Lal\",\n            \"dob\": \"1990-03-09\",\n            \"description\": \"stephen Nedumpalli\"\n        },\n        {\n            \"firstname\": \"Mohan\",\n            \"lastname\": \"Lal\",\n            \"dob\": \"1990-03-09\",\n            \"description\": \"stephen Nedumpalli\"\n        },\n        {\n            \"firstname\": \"Mohan\",\n            \"lastname\": \"Lal\",\n            \"dob\": \"1990-03-09\",\n            \"description\": \"stephen Nedumpalli\"\n        }\n    ]\n}"

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "99604c03-032b-4a98-9bd2-c643fecd6edc"
    }

conn.request("POST", "movies", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
```
