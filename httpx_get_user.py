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
create_user_user_id = create_user_response.json()

login_user_data = {"email": create_user_data["email"], "password": create_user_data["password"]}
login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_user_data)
print(login_user_response.json())
print(login_user_response.status_code)
login_user_token = login_user_response.json()

get_user_headers = {"Authorization": f"Bearer {login_user_token['token']['accessToken']}"}
get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_user_id['user']['id']}", headers=get_user_headers)
print(get_user_response.json())
print(get_user_response.status_code)