from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class ExerciseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str  = Field(default_factory=fake.text)
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.sentence)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class GetExercisesQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    course_id: str = Field(alias="courseId")


class GetExercisesResponseSchema(BaseModel):
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema


class CreateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.sentence)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class CreateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex")
    description: str | None = Field(default_factory=fake.sentence)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)