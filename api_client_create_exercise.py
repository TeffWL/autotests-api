from uuid import UUID

from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict, ExercisesClient, \
    GetExercisesResponseDict, GetExerciseResponseDict, GetExercisesQueryDict, UpdateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Создаем пользователя
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)
# Авторизация + получаем токен
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

#Отправляем файл
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

# Создаем задание для курса
create_exercise_request = CreateExerciseRequestDict(
    title="Задание 5 функции",
    courseId=create_course_response['course']['id'],
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)

# Получаем список задания для определенного курса по id курса  /api/v1/exercises?courseId
# courseId отправляем в переменную что бы не обрщаться к ней из 2вух мест
courseId = create_course_response['course']['id']
# Делаем запрос и передаем courseId
course_exercises_request = GetExerciseResponseDict(courseId=courseId)
# Выводим в консоль ответ
course_exercises_response = exercises_client.get_exercises(course_exercises_request)
print(f'Получение списка заданий по id:{courseId} \n {course_exercises_response}')


# Получаем список задания для определенного курса по exercise_id /api/v1/exercises{exercise_id}
# Делаем запрос и передаем exercise_id
exercise_uuid = create_exercise_response["exercise"]["id"]
course_exercise_response = exercises_client.get_exercise(exercise_uuid)
print(f'Получение задания по exercise_id:{exercise_uuid} \n {course_exercise_response}')



#update_exercise
exercise_uuid = create_exercise_response["exercise"]["id"]
# Редактирование задание для курса
update_exercise_request = UpdateExerciseRequestDict(
    title="Задание 5.1 функции",
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)
update_exercise_response = exercises_client.update_exercise(
    exercise_id=exercise_uuid,
    request=update_exercise_request
)

print(f'Обновления данных задания exercise_id: {exercise_uuid} \n{update_exercise_response}')


# delete
# Делаем запрос и передаем exercise_id
#exercise_uuid = create_exercise_response["exercise"]["id"]
#delete_exercise_response = exercises_client.delete_exercise(exercise_uuid)
#print(f'Удаление exercise_id:{exercise_uuid} \n {delete_exercise_response}')