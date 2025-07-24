from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    courseId: str


class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    exercise: Exercise


class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        return self.get("/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        return self.post("/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        return self.patch(f"/exercises/{exercise_id}", json=request)

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        return self.get_exercises_api(query).json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        return self.get_exercise_api(exercise_id).json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        return self.create_exercise_api(request).json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> GetExerciseResponseDict:
        return self.update_exercise_api(exercise_id, request).json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))