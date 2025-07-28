from pydantic import BaseModel, ConfigDict, Field

from tools.fakers import fake


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: str


class CreateFileResponseSchema(BaseModel):
    file: FileSchema


class CreateFileAPISchema(BaseModel):
    filename: str = Field(default_factory=lambda:f'{fake.uuid4()}.jpg')
    directory: str = Field(default="tests")
    upload_file: str
class GetFileResponseSchema(BaseModel):
    file: FileSchema