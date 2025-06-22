from pydantic import BaseModel, Field
from typing import List, Optional


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
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    title: Optional[str]
    max_score: Optional[int] = Field(alias="maxScore")
    min_score: Optional[int] = Field(alias="minScore")
    order_index: Optional[int] = Field(alias="orderIndex")
    description: Optional[str]
    estimated_time: Optional[str] = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: ExerciseSchema


class DeleteExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа удаления задания.
    """
