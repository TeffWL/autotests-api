from http import HTTPStatus

import httpx

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema

public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(create_user_request)

get_authentication = get_authentication_client()

request = LoginRequestSchema(email=create_user_request.email, password=create_user_request.password)

response = get_authentication.login_api(request)

assert response.status_code == HTTPStatus.OK, 'Некорректный статус-код ответа'

