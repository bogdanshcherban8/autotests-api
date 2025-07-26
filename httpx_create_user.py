import httpx
from tools.fakers import fake

payload={
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=payload)
print(create_user_response.json())
print(create_user_response.status_code)