from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class UserSchema(BaseModel):
    model_config=ConfigDict(populate_by_name=True)
    id: str
    email: str = Field(default_factory=fake.email)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)
class GetUserResponseSchema(BaseModel):
    user:UserSchema
class UpdateUserAPISchema(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        email: str | None = Field(default_factory=fake.email)
        last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
        first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
        middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)
class CreateUserAPISchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config=ConfigDict(populate_by_name=True)
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)

class CreateUserResponseSchema(BaseModel):
    user: UserSchema