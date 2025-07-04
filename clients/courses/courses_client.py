from curlify2 import Curlify
from httpx import Response
from clients.api_client import APIClient
from clients.authentication.authentication_client import AuthenticationClient
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, UpdateCourseRequestSchema, \
    CreateCourseResponseSchema, UpdateCourseResponseSchema, DeleteExerciseResponseShema, \
    GetCourseResponseSchema, GetCoursesResponseSchema
from clients.private_http_builder import get_private_http_client


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    # Добавили новый метод

    def get_courses(self, query: GetCoursesQuerySchema) -> GetCoursesResponseSchema:
        response = self.get_courses_api(query)
        #curl_command = Curlify(response.request).to_curl()
        #print(curl_command)
        return GetCoursesResponseSchema.model_validate_json(response.text)

    def get_course(self, course_id: str) -> GetCourseResponseSchema:
        response = self.get_course_api(course_id)
        #curl_command = Curlify(response.request).to_curl()
        #print(curl_command)
        return GetCourseResponseSchema.model_validate_json(response.text)

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        #curl_command = Curlify(response.request).to_curl()
        #print(curl_command)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def update_course(self, course_id: str, request: UpdateCourseRequestSchema) -> UpdateCourseResponseSchema:
        response = self.update_course_api(course_id, request)
        #curl_command = Curlify(response.request).to_curl()
        #print(curl_command)
        return UpdateCourseResponseSchema.model_validate_json(response.text)

    def delete_course(self, course_id: str) -> DeleteExerciseResponseShema:
        response = self.delete_course_api(course_id)
        return response.json()


def get_courses_client(user: AuthenticationClient) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
