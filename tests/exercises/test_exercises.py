from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from tools.asserations.base import assert_status_code
from tools.asserations.exercises import assert_create_exercise_response
from tools.asserations.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        request = CreateExerciseRequestSchema(
            title="Test Exercise",
            course_id=function_course.response.course.id,
            max_score=100,
            min_score=10
        )
        response = exercises_client.create_exercise_api(request.model_dump(by_alias=True))
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())