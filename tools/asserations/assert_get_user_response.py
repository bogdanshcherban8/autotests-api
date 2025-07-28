from pydantic_create_user import UserSchema
from tools.asserations.assert_user import assert_user


def assert_get_user_response(get_user_response: UserSchema, create_user_response: UserSchema):
    assert_user(get_user_response, create_user_response)