import httpx


def userMe(token):
    headers = {"Authorization": f"Bearer {token}"}
    login_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
    print(login_response.json())
    print(login_response.status_code)

print(userMe(token))