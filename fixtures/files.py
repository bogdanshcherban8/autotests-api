from clients.files.files_client import FilesClient, get_files_client
from clients.files.files_schema import CreateFileAPISchema, CreateFileResponseSchema
from fixtures.users import UserFixture
import pytest
from pydantic import BaseModel
class FileFixture(BaseModel):
    request: CreateFileAPISchema
    response: CreateFileResponseSchema
@pytest.fixture
def files_client(function_user:UserFixture)->FilesClient:
    return get_files_client(function_user.authentication_user)
@pytest.fixture
def function_file(files_client:FilesClient)->FileFixture:
    request=CreateFileAPISchema(upload_file="./testdata/files/image.jpg")
    response=files_client.create_file(request)
    return FileFixture(request=request, response=response)