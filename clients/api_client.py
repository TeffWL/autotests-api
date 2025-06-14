from typing import Any

import httpx
from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Выполняет GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Выполняет POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
        :param files: Файлы для загрузки на сервер.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Выполняет PATCH-запрос (частичное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        """
        Выполняет DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url)


class PublicUsersClient(APIClient):
    def __init__(self, client: Client):
        self.client = client

    def create_user_api(self, url: URL | str, json_data: Any | None = None) -> Response:
        return self.client.post(url, json=json_data)


client = httpx.Client()
users_client = PublicUsersClient(client)
response = users_client.create_user_api(
    url="http://localhost:8000/api/v1/users",
    json_data={
        "email": "dsfs33df332@mail.ru",
        "password": "asdsadasdas",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
)
print(response.text)
