import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.user_schema import GetUserResponseSchema
from fixtures.users import UserFixture
from tools.asserations.assert_get_user_response import assert_get_user_response
import pytest
from clients.users.public_users_client import PublicUsersClient
from clients.users.user_schema import CreateUserAPISchema, CreateUserResponseSchema
from http import HTTPStatus

from tools.asserations.base import assert_status_code
from tools.asserations.schema import validate_json_schema
from tools.asserations.users import assert_create_user_response

from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
class TestUsers:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self, domain: str, public_users_client: PublicUsersClient):
        email = fake.email(domain=domain)
        request = CreateUserAPISchema(email=email)
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_user_me(self, private_users_client: PrivateUsersClient, function_user: UserFixture):
        response = private_users_client.get_user_me_api()
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetUserResponseSchema.model_validate_json(response.text)
        assert_get_user_response(response_data.user, function_user.response.user)
        validate_json_schema(response.json(), response_data.model_json_schema())
