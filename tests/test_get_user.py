from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import GetUserResponseSchema
from fixtures.users import UserFixture
from tools.asserions.base import assert_status_code
from tools.asserions.schema import validate_json_schema
from tools.asserions.users import assert_get_user_response, assert_user


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(
        function_user: UserFixture,  # Используем фикстуру для создания пользователя
        authentication_client: AuthenticationClient,
        private_users_client: PrivateUsersClient):
    # Создаем новго пользователя и получаем метадату
    LoginRequestSchema(email=function_user.email, password=function_user.password)

    #Делаем запрос к GET /api/v1/users/me
    get_user_response = private_users_client.get_user_me_api()

    response_data = GetUserResponseSchema.model_validate_json(get_user_response.text)

    # Асерт сравнения тела на создание и полученного пользователя
    assert_get_user_response(function_user.request, response_data)

    # Асетр сравниваем созданного пользователя и полученного
    assert_user(response_data, function_user.response)

    # Статус код
    assert_status_code(get_user_response.status_code, HTTPStatus.OK)

    # Валидация схемы
    validate_json_schema(get_user_response.json(), response_data.model_json_schema())

    #print('\n new user request',function_user.request,'\nresponse_data', response_data)
