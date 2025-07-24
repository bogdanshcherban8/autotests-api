from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class File(TypedDict):
    id: str
    filename: str
    directory: str
    url: str

class CreateFileResponseDict(TypedDict):
    file:File
class CreateFileAPIDict(TypedDict):
            filename: str
            directory: str
            upload_file: str
class FilesClient(APIClient):
    def get_file_api(self, file_id:str) -> Response:
        return self.get(f"/files/{file_id}")
    def create_file_api(self, request: CreateFileAPIDict):
        return self.post("/files", data=request, files={"upload_file": open(request['upload_file'], "rb")})
    def delete_file_api(self,file_id:str) -> Response:
        return self.delete(f"/files/{file_id}")
    def create_file(self, request:CreateFileAPIDict) ->CreateFileResponseDict:
        response = self.create_file_api(request)
        return response.json()
def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    return FilesClient(client=get_private_http_client(user))
