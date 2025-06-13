import httpx

body = {
    f"email": "test_user@example.com",
    f"password": "test"
}

"""Авторизация"""

def auth(body):
    login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=body)
    login_response_data = login_response.json()
    token = login_response_data["token"]["accessToken"]
    return token

token = auth(body)

"""/api/v1/users/me"""

def userMe(token):
    headers = {"Authorization": f"Bearer {token}"}
    login_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
    print(login_response.json())
    print(login_response.status_code)

print(userMe(token))