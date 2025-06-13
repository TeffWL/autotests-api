import httpx

"""Отправка GET-запроса"""
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)  # 200
print(response.json())

"""Отправка POST-запроса"""
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
} 
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью


"""Отправка данных в application/x-www-form-urlencoded"""
data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)
print('POST')
print(response.json())



""" Передача заголовков"""
headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.json())  # Заголовки включены в ответ


"""Работа с параметрами запроса"""
params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач


"""Отправка файлов"""
files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())  # Ответ с данными о загруженном файле