from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str
class CreateUserRequestModel(BaseModel):
        email: EmailStr
        password: str
        lastName: str
        firstName: str
        middleName: str
class CreateUserResponseSchema(BaseModel):
    user : UserSchema