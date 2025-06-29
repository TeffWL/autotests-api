from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.assert_equal import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ соответсвует тому пользователю которого создали.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user( response: GetUserResponseSchema, request: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание нового пользователя соотвествует тому
    что приходит на get user me.

    :param request: Исходный ответ на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.id, request.user.id, "id")
    assert_equal(response.user.email, request.user.email, "email")
    assert_equal(response.user.last_name, request.user.last_name, "last_name")
    assert_equal(response.user.first_name, request.user.first_name, "first_name")
    assert_equal(response.user.middle_name, request.user.middle_name, "middle_name")


def assert_get_user_response(request: CreateUserRequestSchema, response: GetUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")
