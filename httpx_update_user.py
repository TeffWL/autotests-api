import httpx
from tools.fakers import get_random_email


#Создать пользователя
def new_users():
    email = get_random_email()

    body_users = {
        "email": email,
        "password": "string",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
    new_users_response = httpx.post("http://localhost:8000/api/v1/users", json=body_users)
    new_users_response_data = new_users_response.json()
    print(f"Cоздан пользователь {new_users_response_data}")

    return new_users_response_data


# Авторизация вызов метода api/v1/authentication/login"
def auth_user(new_users_response_data):
    body = {
        "email": new_users_response_data["user"]['email'],
        "password": "string"
    }

    login_response = (httpx.post
                      ("http://localhost:8000/api/v1/authentication/login",json=body))  #POST-запрос к /api/v1/authentication/login успешно выполняется:
    login_response_data = login_response.json()
    token = login_response_data["token"]["accessToken"]

    print("status code:", login_response.status_code)  #Код ответа 200
    print("token:", token)  #Ответ содержит JSON с токенами

    return token


#Изменение пользователя
def update_user(new_users_response_data, token):
    id = new_users_response_data["user"]["id"]
    email = get_random_email()

    body_users = {
        "email": email,
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
    headers = {"Authorization": f"Bearer {token}"}
    update_user_response = (httpx.patch
                            (f"http://localhost:8000/api/v1/users/{id}",
                             headers=headers,
                             json=body_users))
    update_user_response_data = update_user_response.json()

    print(f"Пользователь изменен {update_user_response_data}")


new_users_response_data = new_users() # Создаем пользователя, берем id
token = auth_user(new_users_response_data) # авторизация, логин берем из new_users_response_data
update_user(new_users_response_data, token)# Обновляем пользователя берем токн из auth_user и id из new_users_response_data