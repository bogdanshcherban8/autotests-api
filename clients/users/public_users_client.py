from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
class CreateUserAPIDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    user: User
class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserAPIDict) ->Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/users", json=request)

    def create_user(self, request: CreateUserAPIDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()
def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())