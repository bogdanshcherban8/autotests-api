

from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.user_schema import CreateUserAPISchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserAPISchema) ->Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserAPISchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)
def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())