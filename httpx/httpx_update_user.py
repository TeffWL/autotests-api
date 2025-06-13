import time

import httpx

"""Создать пользователя с помощью POST запроса на эндпоинт /api/v1/users."""
from tools.fakers import get_random_email  # Импортируем функцию для генерации случайного email


def new_users():
    password = get_random_email()
    email = get_random_email()
    body_users = {
        "email": email,
        "password": password,
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
    login_response = httpx.post("http://localhost:8000/api/v1/users", json=body_users)
    login_response_data = login_response.json()
    print(f"Cоздан пользователь {login_response_data}")
    email = login_response_data["user"]["email"]
    id = login_response_data["user"]["id"]
    print(f"Получен пароль и логин,{email}, {password}")
    return password, email, id


"""Авторизация"""

def auth(password, email):
    auth_body = {
        f"email": email,
        f"password": password
    }
    login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=auth_body)
    login_response_data = login_response.json()
    token = login_response_data["token"]["accessToken"]
    print(f'пользователь авторизовван получен токен {token}')
    return token


"""Изменение пользователя"""
def update_user(id, token):
    password = get_random_email()
    email = get_random_email()
    body_users = {
        "email": email,
        "password": password,
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
    headers = {"Authorization": f"Bearer {token}"}
    login_response = httpx.patch(f"http://localhost:8000/api/v1/users/{id}", headers=headers, json=body_users)
    login_response_data = login_response.json()
    print(f"Пользователь изменен {login_response_data}")

password, email, id = new_users()
token = auth(password, email)
update_user(id, token)
