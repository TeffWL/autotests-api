from typing import List, Any
from pydantic import BaseModel, EmailStr, HttpUrl, ConfigDict, Field
from pydantic.alias_generators import to_camel
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class GetCoursesPatchSchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    course_id: str



class GetCourseSchema(BaseModel):
    """
    GET /api/v1/courses
    GET /api/v1/courses{id}
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema


class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )

    title: str
    description: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    estimated_time: str = Field(alias="estimatedTime")
    preview_fileId: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class GetCoursesResponseSchema(BaseModel):
    courses: List[GetCourseSchema]


class GetCourseResponseSchema(BaseModel):
    course: GetCourseSchema


class CreateCourseResponseSchema(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )
    course: GetCourseSchema


class UpdateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateCourseResponseSchema(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )
    course: GetCourseSchema

class DeleteExerciseResponseShema(BaseModel):
    """
    Описание структуры ответа обновления задания.
    """
    None


class DetailItem(BaseModel):
    """Модель для элемента в списке detail"""
    loc: List[Any]  # Список с произвольными значениями
    msg: str  # Сообщение об ошибке
    type: str  # Тип ошибки


class ValidationError(BaseModel):
    """Основная модель для структуры деталей ошибок"""
    detail: List[DetailItem]  # Список элементов DetailItem
