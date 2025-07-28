from clients.courses.courses_schema import UpdateCourseAPISchema, UpdateCourseResponseSchema
from tools.asserations.base import assert_equal


def assert_update_course_response(request:UpdateCourseAPISchema, response:UpdateCourseResponseSchema):
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")