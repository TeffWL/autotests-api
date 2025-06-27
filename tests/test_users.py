from http import HTTPStatus
import pytest

from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.asserions.base import assert_status_code
from tools.asserions.schema import validate_json_schema
from tools.asserions.users import assert_create_user_response


# Импортируем функцию проверки статус-кода
@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):  # Используем фикстуру API клиента
    # Удалили инициализацию API клиента из теста
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())