from pydantic import BaseModel, Field, ConfigDict


from clients.files.files_schema import FileSchema

from clients.users.user_schema import UserSchema
from tools.asserations.assert_user import assert_user
from tools.asserations.base import assert_equal, assert_length
from tools.asserations.files import assert_file

from tools.fakers import fake


class CourseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.sentence)
    preview_file: FileSchema = Field(alias="previewFile", default_factory=fake.uuid4)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    created_by_user: UserSchema = Field(alias="createdByUser", default_factory=fake.uuid4)


class CreateCoursesResponseSchema(BaseModel):
    course: CourseSchema


class GetCoursesAPISchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")

class CreateCoursesAPISchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.sentence)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)


class UpdateCourseAPISchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.sentence)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateCourseResponseSchema(BaseModel):
    course: CourseSchema


class GetCoursesResponseSchema(BaseModel):
    courses: list[CourseSchema]


def assert_course(actual: CourseSchema, expected: CourseSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


def assert_get_courses_response(get_courses_response: GetCoursesResponseSchema,
                                create_course_responses: list[CreateCoursesResponseSchema]):
    assert_length(get_courses_response.courses, create_course_responses, "courses")
    for index, create_course_responses in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_responses.course)
def assert_create_course_response(
    request: CreateCoursesAPISchema,
    response: CreateCoursesResponseSchema
):
    course = response.course

    assert_equal(course.title, request.title, "title")
    assert_equal(course.description, request.description, "description")
    assert_equal(course.max_score, request.max_score, "max_score")
    assert_equal(course.min_score, request.min_score, "min_score")
    assert_equal(course.estimated_time, request.estimated_time, "estimated_time")

    assert course.preview_file is not None, "preview_file is missing in response"
    assert_equal(course.preview_file.id, request.preview_file_id, "preview_file.id")

    assert course.created_by_user is not None, "created_by_user is missing in response"
    assert_equal(course.created_by_user.id, request.created_by_user_id, "created_by_user.id")