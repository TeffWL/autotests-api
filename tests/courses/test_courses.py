from http import HTTPStatus
import allure
import pytest
from allure_commons.types import Severity

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.files import assert_file
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_user


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.COURSES)  # Добавили feature
class TestCourses:
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get courses")
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    def test_create_course(self,
                           courses_client: CoursesClient,
                           function_user: UserFixture,
                           function_course: CourseFixture,
                           function_file: FileFixture
                           ):
        # Формируем параметры запроса
        request_data = CreateCourseRequestSchema(
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id
        )
        # Отправляем POST-запрос на создание курса
        response = courses_client.create_course_api(request_data)

        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем параметры запроса и ответа
        assert_create_course_response(request_data, response_data)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITIES)  # Добавили тег
    @allure.title("Get courses")
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    def test_get_courses(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_course: CourseFixture
    ):
        # Формируем параметры запроса, передавая user_id
        query = GetCoursesQuerySchema(userId=function_user.response.user.id)
        # Отправляем GET-запрос на получение списка курсов
        response = courses_client.get_courses_api(query)
        # Десериализуем JSON-ответ в Pydantic-модель
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список курсов соответствует ранее созданным курсам

        assert_get_courses_response(response_data, [function_course.response])

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)  # Добавили тег
    @allure.title("Update course")
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        # Формируем данные для обновления
        request = UpdateCourseRequestSchema()
        # Отправляем запрос на обновление курса
        response = courses_client.update_course_api(function_course.response.course.id, request)
        # Преобразуем JSON-ответ в объект схемы
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        # Проверяем статус-код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что данные в ответе соответствуют запросу
        assert_update_course_response(request, response_data)

        # Валидируем JSON-схему ответа
        validate_json_schema(response.json(), response_data.model_json_schema())
