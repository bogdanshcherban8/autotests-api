import httpx
login_payload = {
  "email": "zub@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login_response:", login_response_data)
print("Status_code:", login_response.status_code)

access_token = login_response_data["token"]["accessToken"]
headers = {"Authorization": f"Bearer {access_token}"}

user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_me_data = user_me_response.json()
print("User_me_response:", user_me_data)
print("Status_code:", user_me_response.status_code)