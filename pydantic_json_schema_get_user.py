from clients.users.public_users_client import (
    get_public_users_client,
    CreateUserAPISchema,
)
from clients.users.private_users_client import (
    get_private_users_client,
)
from tools.asserations.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserAPISchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string",
)
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_data = create_user_response.json()

user_id = create_user_data["user"]["id"]

private_users_client = get_private_users_client(create_user_request)
get_user_response = private_users_client.get_user_api(user_id)

from clients.users.user_schema import GetUserResponseSchema
get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

print("✅ JSON schema валидация прошла успешно.")