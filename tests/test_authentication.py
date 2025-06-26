from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.asserions.authentication import assert_login_response
from tools.asserions.base import assert_status_code
from tools.asserions.schema import validate_json_schema


def test_login():
     #Создаем нового пользователя
    public_users_client = get_public_users_client()
    create_user_request = CreateUserRequestSchema()
    create_user_response = public_users_client.create_user(create_user_request)

    get_authentication = get_authentication_client()
      #Аунтификация
    authentication_user_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
      # Получаем ответ
    authentication_user_response = get_authentication.login_api(authentication_user_request)
      #Десериализация json
    login_response_data = LoginResponseSchema.model_validate_json(authentication_user_response.text)
      #Проверяем status_code
    assert_status_code(authentication_user_response.status_code, HTTPStatus.OK)
      # Проверка на  корректность тела ответа
    assert_login_response(login_response_data)
      # Валидация JSON-схемы
    validate_json_schema(authentication_user_response.json(), login_response_data.model_json_schema())
