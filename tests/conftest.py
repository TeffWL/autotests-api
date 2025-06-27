import pytest  # Импортируем pytest
from httpx import Response, Client
from pydantic import EmailStr, BaseModel

# Импортируем API клиенты
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


# Модель для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password

    def authentication_user(self) -> AuthenticationUserSchema:
        return self.AuthenticationUserSchema


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def authentication_client() -> AuthenticationClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def public_users_client() -> PublicUsersClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()


# Фикстура для создания пользователя
@pytest.fixture
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)  # Возвращаем все нужные данные


@pytest.fixture
def authentication_user(function_user: UserFixture, authentication_client: AuthenticationClient) -> Response:
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    response = authentication_client.login_api(request)
    return response


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    """Фикстура для создания инициализированного PrivateUsersClient"""
    auth_user = AuthenticationUserSchema(
        email=function_user.email,
        password=function_user.password
    )
    return get_private_users_client(auth_user)