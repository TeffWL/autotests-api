import allure
from allure_commons.types import Severity

from http import HTTPStatus
import pytest
from clients.authentication.authentication_client import AuthenticationClient
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercise_shema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExercisesQuerySchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, DeleteExerciseResponseSchema, \
    GetExercisesResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.users.private_users_client import PrivateUsersClient
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercise import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.EXERCISES)  # Добавили feature
class TestExercises:

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create exercise")
    @allure.severity(Severity.BLOCKER)
    def test_create_exercise(self,
                             function_user: UserFixture,
                             authentication_client: AuthenticationClient,
                             exercises_client: ExercisesClient,
                             function_course: CourseFixture,
                             private_users_client: PrivateUsersClient):
        request_data = CreateExerciseRequestSchema(
            courseId=function_course.response.course.id,
        )

        # Отправляем POST-запрос на создание курса
        response = exercises_client.create_exercise_api(request_data)

        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем параметры запроса и ответа
        assert_create_exercise_response(request_data, response_data)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get exercise")
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    def test_get_exercise(self,
                          function_exercise: ExerciseFixture,
                          exercises_client: ExercisesClient):
        requests_data = function_exercise.response.exercise.id

        response = exercises_client.get_exercise_api(requests_data)

        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем, что задание соответствует ранее созданному заданию
        assert_get_exercise_response(response_data, function_exercise.response)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update exercise")
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_update_exercise(self,
                             function_exercise: ExerciseFixture,
                             exercises_client: ExercisesClient):
        request_data = UpdateExerciseRequestSchema()
        uuid = function_exercise.response.exercise.id

        response = exercises_client.update_exercise_api(uuid, request_data)

        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем, запрос соответсвует ответу
        assert_update_exercise_response(request_data, response_data)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Delete exercise")
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_delete_exercise(self,
                             function_exercise: ExerciseFixture,
                             exercises_client: ExercisesClient):
        # Cоздаем запись, получаем id
        uuid = function_exercise.response.exercise.id
        # Делаем запрос на удалениее ранее созданной записи
        response = exercises_client.delete_exercise_api(uuid)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Делаем запрос на получении ранее созданной и удаленной записи
        response_get = exercises_client.get_exercise_api(uuid)
        # Проверяем схему
        get_response_data = InternalErrorResponseSchema.model_validate_json(response_get.text)
        # Проверяем что ответ 404 не найдено
        assert_exercise_not_found_response(get_response_data)

    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get exercises")
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    def test_get_exercises(self,
                           function_exercise: ExerciseFixture,
                           exercises_client: ExercisesClient):
        # Создаем схему запроса с нужными параметрами
        query = GetExercisesQuerySchema(courseId=function_exercise.response.exercise.course_id)

        response = exercises_client.get_exercises_api(query=query)

        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_get_exercises_response(response_data, function_exercise.response)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())
