from clients.api_client import APIClient
from httpx import Response
from clients.courses.courses_schema import CreateCoursesAPISchema, UpdateCourseAPISchema, \
    CreateCoursesResponseSchema, GetCoursesAPISchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class CoursesClient(APIClient):
    def get_courses_api(self, query: GetCoursesAPISchema) -> list:
        return self.get("/courses", params=query.model_dump(by_alias=True))
    def get_course_api(self, course_id:str)->Response:
        return self.get(f"/courses/{course_id}")
    def create_course_api(self, request:CreateCoursesAPISchema) -> Response:
        return self.post("/courses", json=request)
    def update_course_api(self, course_id:str, request: UpdateCourseAPISchema)->Response:
        return self.patch(f'/courses/{course_id}', json=request)
    def delete_course_api(self, course_id:str)->Response:
        return self.delete(f'/courses/{course_id}')
    def create_course(self, request:CreateCoursesAPISchema) -> CreateCoursesResponseSchema:
        response = self.create_course_api(request.model_dump(by_alias=True))
        return CreateCoursesResponseSchema.model_validate_json(response.text)
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))
