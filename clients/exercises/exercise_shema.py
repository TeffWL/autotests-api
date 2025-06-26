from pydantic import BaseModel, Field
from typing import List, Optional

from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение задания.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    course_id: str = Field(alias="courseId")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка заданий.
    """
    exercises: List[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    title: Optional[str] = Field(default_factory=fake.sentence)
    course_id: Optional[str] = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: Optional[int] = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: Optional[int] = Field(alias="minScore", default_factory=fake.min_score)
    order_index: Optional[int] = Field(alias="orderIndex", default_factory=fake.integer)
    description: Optional[str] = Field(default_factory=fake.text)
    estimated_time: Optional[str] = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: ExerciseSchema


class DeleteExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа удаления задания.
    """
