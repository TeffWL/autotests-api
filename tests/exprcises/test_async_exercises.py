from curlify2 import Curlify
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
from tools.assertions.base import assert_status_code
from tools.assertions.exercise import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.asyncio
class TestExercises:
    @pytest.mark.exercises
    @pytest.mark.regression
    async def test_create_exercise(self,
                                 function_user: UserFixture,
                                 authentication_client: AuthenticationClient,
                                 exercises_client: ExercisesClient,
                                 function_course: CourseFixture,
                                 private_users_client: PrivateUsersClient):
        request_data = CreateExerciseRequestSchema(
            courseId=function_course.response.course.id,
        )

        # Отправляем POST-запрос на создание курса
        response = await exercises_client.create_exercise_api(request_data)

        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем параметры запроса и ответа
        assert_create_exercise_response(request_data, response_data)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    async def test_get_exercise(self,
                              function_exercise: ExerciseFixture,
                              exercises_client: ExercisesClient):
        requests_data = function_exercise.response.exercise.id

        response = await exercises_client.get_exercise_api(requests_data)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        curl_command = Curlify(response.request).to_curl()
        print(curl_command)

        # Проверяем, что задание соответствует ранее созданному заданию
        assert_get_exercise_response(response_data, function_exercise.response)
        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())

    async def test_update_exercise(self,
                                 function_exercise: ExerciseFixture,
                                 exercises_client: ExercisesClient):
        request_data = UpdateExerciseRequestSchema()
        uuid = function_exercise.response.exercise.id

        response = await exercises_client.update_exercise_api(uuid, request_data)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем, запрос соответсвует ответу
        assert_update_exercise_response(request_data, response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())

    async def test_delete_exercise(self,
                                 function_exercise: ExerciseFixture,
                                 exercises_client: ExercisesClient):
        # Cоздаем запись, получаем id
        uuid = function_exercise.response.exercise.id
        # Делаем запрос на удалениее ранее созданной записи
        response = await exercises_client.delete_exercise_api(uuid)
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Делаем запрос на получении ранее созданной и удаленной записи
        response_get = await exercises_client.get_exercise_api(uuid)
        get_response_data = InternalErrorResponseSchema.model_validate_json(response_get.text)
        assert_exercise_not_found_response(get_response_data)

    async def test_get_exercises(self,
                               function_exercise: ExerciseFixture,
                               exercises_client: ExercisesClient):
        query = GetExercisesQuerySchema(courseId=function_exercise.response.exercise.course_id)
        response = await exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, function_exercise.response)
        validate_json_schema(response.json(), response_data.model_json_schema())