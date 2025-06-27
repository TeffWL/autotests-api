from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercise_shema import CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesQuerySchema
from clients.exercises.exercises_client import (get_exercises_client)
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import fake

# Создаем пользователя
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_response = public_users_client.create_user(create_user_request)
# Авторизация + получаем токен
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

#Отправляем файл
create_file_request = CreateFileRequestSchema(
    upload_file="/test_data/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# POST /api/v1/exercises
create_exercise_request = CreateExerciseRequestSchema(
    courseId=create_course_response.course.id,
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Задание для курса:', create_exercise_response)


# GET /api/v1/exercises/qury
courseId = create_course_response.course.id
create_exercises_request = GetExercisesQuerySchema(courseId=courseId)
create_exercises_response = exercises_client.get_exercises(create_exercises_request)
print(f'Получение списка заданий по id:{courseId} \n {create_exercises_response}')


# GET /api/v1/exercises/{exercise_id}
exercise_uuid = create_exercise_response.exercise.id
course_exercise_response = exercises_client.get_exercise(exercise_uuid)
print(f'Получение задания по exercise_id:{exercise_uuid} \n {course_exercise_response}')



# PATCH /api/v1/exercises/{exercise_id}
exercise_uuid = create_exercise_response.exercise.id
update_exercise_request = UpdateExerciseRequestSchema(
)
update_exercise_response = exercises_client.update_exercise(
    exercise_id=exercise_uuid,
    request=update_exercise_request
)

print(f'Обновления данных задания exercise_id: {exercise_uuid} \n{update_exercise_response}')



# delete
# Делаем запрос и передаем exercise_id
exercise_uuid = create_exercise_response.exercise.id
delete_exercise_response = exercises_client.delete_exercise(exercise_uuid)
print(f'Удаление exercise_id:{exercise_uuid} \n {delete_exercise_response}')