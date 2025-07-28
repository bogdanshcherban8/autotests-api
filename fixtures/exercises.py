import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.users import UserFixture
from fixtures.files import FileFixture
from fixtures.courses import CourseFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
    exercises_client: ExercisesClient,
    function_user: UserFixture,
    function_file: FileFixture,
    function_course: CourseFixture,
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(
        course_id=function_course.response.id,
        file_id=function_file.response.id,
    )
    response = exercises_client.create_exercise_api(request)
    response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

    return ExerciseFixture(request=request, response=response_data)
