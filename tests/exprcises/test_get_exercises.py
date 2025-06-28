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


def test_get_user_me(
        function_user: UserFixture,
        authentication_client: AuthenticationClient,
        private_users_client: PrivateUsersClient):

    LoginRequestSchema(email=function_user.email, password=function_user.password)

    #Делаем запрос к GET /api/v1/users/me
    get_user_response = private_users_client.get_user_me_api()

    response_data = GetUserResponseSchema.model_validate_json(get_user_response.text)
