from clients.users.user_schema import CreateUserAPISchema, CreateUserResponseSchema
from tools.asserations.base import assert_equal


def assert_create_user_response(request:CreateUserAPISchema, response: CreateUserResponseSchema):
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")