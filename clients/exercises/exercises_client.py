from httpx import Response
from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, GetExerciseResponseSchema, CreateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class ExercisesClient(APIClient):
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        return self.get("/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        return self.post("/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        return self.patch(f"/exercises/{exercise_id}", json=request)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        return self.get_exercises_api(query).json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        return self.get_exercise_api(exercise_id).json()

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        return self.create_exercise_api(request.model_dump(by_alias=True))

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> GetExerciseResponseSchema:
        return self.update_exercise_api(exercise_id, request).json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
