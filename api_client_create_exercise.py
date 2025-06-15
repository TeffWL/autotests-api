from api_client_create_course import courses_client
from clients.courses.courses_client import CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, ExercisesClient, CreateExercisesRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_files_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="/Users/msemushev/Desktop/auto/autotests-api/test_data/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)


# Создаем задание
create_exercise_request = CreateExercisesRequestDict(
    title="Установка PyCharm",
    courseId=create_course_response["course"]["id"], # Берем id из создания курса и по нему создаем задание
    maxScore=100,
    minScore=10,
    orderIndex=10,
    description="Установка PyCharm",
    estimatedTime="1h",
)
create_exercise_response = exercise_client.create_exercises_api(create_exercise_request)
print('Create exercise data:', create_exercise_response.json()) # <- без json() не показывает ответ в отличии от create_course_response

"""
Create file data: {'file': {'id': '02d3eeea-5969-4af8-87b8-3f7b844c9c80', 'filename': 'image.png', 'directory': 'courses', 'url': 'http://localhost:8000/static/courses/image.png'}}
Create course data: {'course': {'id': '8e8c3b4d-a536-4548-8e98-d5da1a810ea9', 'title': 'Python', 'maxScore': 100, 'minScore': 10, 'description': 'Python API course', 'previewFile': {'id': '02d3eeea-5969-4af8-87b8-3f7b844c9c80', 'filename': 'image.png', 'directory': 'courses', 'url': 'http://localhost:8000/static/courses/image.png'}, 'estimatedTime': '2 weeks', 'createdByUser': {'id': 'a0e0c6cf-aebe-4cd9-a0c0-fcdab66f0d05', 'email': 'test.1750010369.539841@example.com', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}}
Create exercise data: {'exercise': {'id': '49706d23-5bd5-492b-b14d-cb1a3e6ebdae', 'title': 'Установка PyCharm', 'courseId': '8e8c3b4d-a536-4548-8e98-d5da1a810ea9', 'maxScore': 100, 'minScore': 10, 'orderIndex': 10, 'description': 'Установка PyCharm', 'estimatedTime': '1h'}}

"""