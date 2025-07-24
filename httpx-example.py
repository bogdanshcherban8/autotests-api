import httpx

reposnse = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(reposnse.status_code)
print(reposnse.json())

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.request.headers)
print(response.json())

data = {"username": "test_user", "password": "<PASSWORD>"}
response = httpx.post("https://httpbin.org/post", data=data)

print(response.status_code)
print(response.request.headers)
print(response.json())

headers = {"Authorization": "Bearer token"}
response = httpx.get("https://httpbin.org/get", headers = headers)
print(response.request.headers)
print(response.json())

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos?", params=params)
print(response.url)
print(response.json())

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())

with httpx.Client() as client:
    response_1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response_2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response_1.json())
print(response_2.json())

client = httpx.Client(headers = {"Authorization": "Bearer token"})
response = client.get("https://httpbin.org/get")
print(response.json())

response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")

