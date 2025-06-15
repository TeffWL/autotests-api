from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.files.files_client import File
from clients.users.private_users_client import User


# Добавили описание структуры курса

class Exercises(TypedDict):
    """
    Описание структуры задач.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File  # Вложенная структура файла
    estimatedTime: str
    createdByUser: User  # Вложенная структура пользователя

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    exercise_id: str


class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание заданий.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление заданий.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


# Добавили описание структуры запроса на создание курса
class CreateExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа создания курса.
    """
    exercises: list[Exercises]


class ExercisesClient(APIClient):
    """
       Клиент для работы с /api/v1/exercises

       """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: string($uuid)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api_id(self, exercise_id, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param exercise_id: Идентификатор курса.
        :param query: string($uuid)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises{exercise_id}", params=query)

    def create_exercises_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Создание задания.

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime,
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercises_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Обновления данных задания..

        :param exercise_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime,
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод удаления курса.

        :param exercise_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> CreateExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
