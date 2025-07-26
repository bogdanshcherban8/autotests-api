import httpx
from tools.fakers import fake

create_user_data= {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_data)
print(create_user_response.json())
print(create_user_response.status_code)

login_user_data = {"email": create_user_data["email"], "password": create_user_data["password"]}

login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_user_data)
print(login_user_response.json())
print(login_user_response.status_code)

patch_user_data = {
  "email": "123@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
login_token = login_user_response.json()
access_token = {"Authorization": f"Bearer {login_token['token']['accessToken']}"}
create_user_id = create_user_response.json()

patch_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_id['user']['id']}", headers=access_token, json=patch_user_data)
print(patch_user_response.json())
print(patch_user_response.status_code)