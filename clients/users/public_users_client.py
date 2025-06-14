import sys
import time
from typing import Any
import httpx
from apiclient import APIClient
from httpx import Client, URL, Response


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

class PublicUsersClient(APIClient):
    def __init__(self, client: Client):
        self.client = client

    def create_user_api(self, url: URL | str, json_data: Any | None = None) -> Response:
        return self.client.post(url, json=json_data)

    """
            Создание нового пользователя.

            Параметры:
                url (URL | str): URL 
                json_data (Any | None)
        
                Пример  json_data:
                ...     json_data={
                ...         "email": "user@example.com",
                ...         "password": "string",
                ...         "lastName": "string",
                ...         "firstName": "sitrng",
                ...         "middleName": "string"
                ... )
                
            Возвращает:
                Response: Обьект users {id,email,lastname,firstname,middlename}

    
            """


client = httpx.Client()
users_client = PublicUsersClient(client)


response = users_client.create_user_api(
    url="http://localhost:8000/api/v1/users",
    json_data={
        "email": get_random_email(),
        "password": "asdsadasdas",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
)
print(response.text)
