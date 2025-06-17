import httpx

# Параметры
#Лишние f-строки - хотел брать параметры из.env
# но подумал что это лишнее и просто забыл удалить

body = {
    "email": "test_user@example.com",
    "password": "test"
}

# Авторизация вызов метода api/v1/authentication/login"
def auth_user(body):
    #Запрос авторизации
    login_response = (httpx.post
                      ("http://localhost:8000/api/v1/authentication/login",
                       json=body)) #POST-запрос к /api/v1/authentication/login успешно выполняется:
    # Берем из ответа токен
    login_response_data = login_response.json()
    token = login_response_data["token"]["accessToken"]
    #json ответ и статус код
    print("status code:", login_response.status_code) #Код ответа 200
    print("token:", token )#Ответ содержит JSON с токенами
    #Возвращаем токен
    return token


token = auth_user(body)


# Вызов метода /api/v1/users/me" с передачей token
def get_user_info(token):
    headers = {"Authorization": f"Bearer {token}"}
    # GET-запрос к /api/v1/users/me успешно выполняется:
    user_response_data = (httpx.get
                          ("http://localhost:8000/api/v1/users/me",
                           headers=headers))
    # Ответ содержит JSON с данными пользователя
    print(user_response_data.json())
    # Код ответа 200
    print(user_response_data.status_code)



get_user_info(token) #В консоль выводится JSON-ответ от сервера с данными о пользователе и статус код ответа
