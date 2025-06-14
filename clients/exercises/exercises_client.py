from typing import TypedDict

from apiclient import APIClient
from httpx import Response


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


class CoursesClient(APIClient):
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

    def get_exercises_api(self, exercises_id: str) -> Response:
        """
        Получение информации о задании по exercise_id.

        :param exercise_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercises_id}")

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