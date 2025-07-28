from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseAPISchema, UpdateCourseResponseSchema, GetCoursesAPISchema, \
    GetCoursesResponseSchema, assert_get_courses_response, CreateCoursesResponseSchema, CreateCoursesAPISchema, \
    assert_create_course_response
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.asserations.base import assert_status_code
from tools.asserations.courses import assert_update_course_response
from tools.asserations.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_get_courses(self, courses_client: CoursesClient, function_user:UserFixture, function_course:CourseFixture):
        query= GetCoursesAPISchema(user_id=function_user.response.user.id)
        response=courses_client.get_courses_api(query)
        response_data= GetCoursesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])
        validate_json_schema(response.json(), response_data.model_json_schema())
    def test_update_course(self, courses_client: CoursesClient, function_course:CourseFixture):
        request=UpdateCourseAPISchema()
        response=courses_client.update_course_api(function_course.response.course.id, request.model_dump(by_alias=True))
        response_data=UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_create_course(self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_file: FileFixture
    ):
        request = CreateCoursesAPISchema(
            title="Sample Course",
            description="Test course",
            max_score=100,
            min_score=10,
            estimated_time="2h",
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id
        )

        response = courses_client.create_course(request)

        assert_create_course_response(request, response)
        validate_json_schema(response.model_dump(by_alias=True), response.model_json_schema())