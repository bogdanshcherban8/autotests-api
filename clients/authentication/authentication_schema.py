from pydantic import BaseModel, EmailStr, Field

from tools.fakers import fake


class TokenSchema(BaseModel):
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")
class LoginResponseSchema(BaseModel):
    token:TokenSchema
class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
class RefreshTokenSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken", default_factorty=fake.sentence)