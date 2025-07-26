
from clients.users.public_users_client import get_public_users_client, CreateUserAPISchema, CreateUserResponseSchema
from tools.asserations.schema import validate_json_schema
from tools.fakers import fake
import jsonschema
public_users_client = get_public_users_client()

create_user_request = CreateUserAPISchema(
email= fake.email(),
  password= "string",
  last_name= "string",
  first_name= "string",
  middle_name= "string"
)
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema=CreateUserResponseSchema.model_json_schema()


validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)