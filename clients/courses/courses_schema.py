from typing import List, Any
from pydantic import BaseModel, EmailStr, HttpUrl, ConfigDict, Field
from pydantic.alias_generators import to_camel
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


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


class CourseSchema(BaseModel):
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
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Добавили генерацию случайного заголовка
    title: str = Field(default_factory=fake.sentence)
    # Добавили генерацию случайного максимального балла
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    # Добавили генерацию случайного минимального балла
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    # Добавили генерацию случайного описания
    description: str = Field(default_factory=fake.text)
    # Добавили генерацию случайного предполагаемого времени прохождения курса
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    # Добавили генерацию случайного идентификатора файла
    preview_file_id: str = Field(alias="previewFileId")  #, default_factory=fake.uuid4)
    # Добавили генерацию случайного идентификатора пользователя
    created_by_user_id: str = Field(alias="createdByUserId")  #, default_factory=fake.uuid4)


class GetCoursesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка курсов.
    """
    courses: list[CourseSchema]


class GetCourseResponseSchema(BaseModel):
    course: CourseSchema


class CreateCourseResponseSchema(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Добавили генерацию случайного заголовка
    title: str | None = Field(default_factory=fake.sentence)
    # Добавили генерацию случайного максимального балла
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    # Добавили генерацию случайного минимального балла
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    # Добавили генерацию случайного описания
    description: str | None = Field(default_factory=fake.text)
    # Добавили генерацию случайного предполагаемого времени прохождения курса
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateCourseResponseSchema(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )
    course: CourseSchema


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
