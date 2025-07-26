

from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.user_schema import UpdateUserAPISchema, GetUserResponseSchema


class PrivateUsersClient(APIClient):
    def get_user_me_api(self) ->Response:
        return self.get("/users/me")
    def get_user_api(self, user_id:str) ->Response:
        return self.get(f"/users/{user_id}")
    def update_user_api(self, user_id: str, request: UpdateUserAPISchema) -> Response:
        return self.patch(f"/users/{user_id}", json=request)
    def delete_user_api(self, user_id:str) ->Response:
        return self.delete(f"/users/{user_id}")
    def get_user(self, user_id:str)-> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return response.json()
def get_private_users_client(user:AuthenticationUserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))

