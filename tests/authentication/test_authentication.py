from http import HTTPStatus

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from clients.users.public_users_client import PublicUsersClient
from fixtures.users import UserFixture
from tools.asserations.authentication import assert_login_response
from tools.asserations.base import assert_status_code
from tools.asserations.schema import validate_json_schema
import pytest


@pytest.mark.authentication
@pytest.mark.regression
class TestAuthentication:
    def test_login(self, function_user: UserFixture, public_users_client: PublicUsersClient,
                   authentication_client: AuthenticationClient):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
