from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.asserations.base import assert_equal


def assert_create_exercise_response(
    request: CreateExerciseRequestSchema,
    response: CreateExerciseResponseSchema
):
    exercise = response.exercise

    assert_equal(exercise.title, request.title, "title")
    assert_equal(exercise.course_id, request.course_id, "course_id")
    assert_equal(exercise.max_score, request.max_score, "max_score")
    assert_equal(exercise.min_score, request.min_score, "min_score")