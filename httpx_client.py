import httpx
from tools.fakers import fake

create_user_data = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_data)
print(create_user_response.json())
print(create_user_response.status_code)

login_user_data = {"email":create_user_data["email"], "password": create_user_data["password"]}
login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_user_data)
print(login_user_response.json())
print(login_user_response.status_code)
login_token = login_user_response.json()

client = httpx.Client(base_url="http://localhost:8000/api/v1", timeout=100, headers = {"Authorization": f"Bearer {login_token['token']['accessToken']}"})
response = client.get("/users/me")
print(response.text)
print(response.status_code)