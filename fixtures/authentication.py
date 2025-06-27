import pytest
from httpx import Response
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from fixtures.users import UserFixture


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture
def authentication_user(function_user: UserFixture, authentication_client: AuthenticationClient) -> Response:
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    response = authentication_client.login_api(request)
    return response
