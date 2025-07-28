from clients.courses.courses_client import CoursesClient, get_courses_client
import pytest
from clients.courses.courses_schema import CreateCoursesAPISchema, CreateCoursesResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from pydantic import BaseModel

class CourseFixture(BaseModel):
    request:CreateCoursesAPISchema
    response: CreateCoursesResponseSchema

@pytest.fixture
def courses_client(function_user:UserFixture)->CoursesClient:
    return get_courses_client(function_user.authentication_user)
@pytest.fixture
def function_course(courses_client:CoursesClient, function_user:UserFixture, function_file:FileFixture)-> CourseFixture:
    request=CreateCoursesAPISchema(preview_file_id=function_file.response.file.id, created_by_user_id=function_user.response.user.id)
    response=courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
