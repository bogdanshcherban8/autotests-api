import httpx
from tools.fakers import fake

create_user_data = {"email": fake.email(),
                    "password": "string",
                    "lastName": "string",
                    "firstName": "string",
                    "middleName": "string"}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_data)
print(create_user_response.json())
print(create_user_response.status_code)
create_user_id = create_user_response.json()

login_user_data = {"email": create_user_data["email"], "password": create_user_data["password"]}

login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_user_data)
print(login_user_response.json())
print(login_user_response.status_code)
login_token = login_user_response.json()

create_file_headers = {"Authorization": f'Bearer {login_token["token"]["accessToken"]}'}
create_file_response = httpx.post("http://localhost:8000/api/v1/files",
                                  data={"filename": "image.jpg", "directory": "courses"},
                                  files={"upload_file": open("./testdata/files/image.jpg", "rb")},
                                  headers=create_file_headers)
create_file_response_data = create_file_response.json()
print(create_file_response_data)
print(create_file_response.status_code)