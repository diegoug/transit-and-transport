# Transit and Transport
This project is a web application and API for managing people, vehicles, officials, and registering traffic infractions.

## Requirements
Docker
docker-compose

## Commands

### start-development
``` bash
make start-development [-- --build]
```
This command starts the necessary containers for the application and database.

The --build flag is optional, and is used to build the application image if changes have been made to the code.

### migrate-development
``` bash
make migrate-development
```

This command applies the necessary migrations to the database. Before running this command, start-development must have been executed.

### stop-development
``` bash
make stop-development
```
This command stops the containers of the application and the database.

## Web URLs
- http://localhost:5000/admin/person
- http://localhost:5000/admin/vehicles
- http://localhost:5000/admin/officials

## API URLs

### POST /api/login

To obtain an access token, a POST request must be sent to this URL with a multipart/form-data form. The username and password fields must be completed with the credentials of a user registered in the database.

Example:
``` python
import requests

url = "http://localhost:5000/api/login"

payload = {'username': 'DiegoUG',
'password': 'my_password'}
files = [

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

### POST /api/infraction
To register an infraction, a POST request must be sent to this URL with a JSON in the request body. The JSON must contain the license_plate, timestamp, and comments fields. In addition, the request must be authenticated with an access token.

Example
``` python
import requests

url = "http://localhost:5000/api/infraction"

payload = {'license_plate': 'ABC123',
'timestamp': '2022-02-22 12:00:00',
'comments': 'Parked in a forbidden place'}
headers = {
'Authorization': 'Bearer <access_token>'
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)
```

### GET /api/generate_report/<email>

To generate a report of a user's infractions, a GET request must be sent to this URL with the user's email as a parameter. In addition, the request must be authenticated with an access token.

Example
``` python
import requests

url = "http://localhost:5000/api/generate_report/john@example.com"

headers = {
'Authorization': 'Bearer <access_token>'
}

response = requests.request("GET", url, headers=headers)

print(response.text)
```