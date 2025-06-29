from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, GetCoursesQuerySchema, GetCoursesPatchSchema, \
    UpdateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(create_user_request)
print('Создан пользователь', create_user_response)
# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestSchema(
    upload_file="/testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# post /api/v1/courses
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

#get /api/v1/courses?qury
userId = create_course_response.course.created_by_user.id
get_courses_view_request = GetCoursesQuerySchema(userId=userId)
get_courses_response = courses_client.get_courses(get_courses_view_request)
print(f'Получение списка заданий по id:{userId} \n {get_courses_response}')

#get /api/v1/courses/{course_id}
course_id = create_course_response.course.id
get_courses_view_patch_request = courses_client.get_course(course_id)
print(f'Получение заданий по course_id:{course_id} \n {get_courses_view_patch_request}')

#patch /api/v1/courses/{course_id}

update_course_request = UpdateCourseRequestSchema(
)
course_id = create_course_response.course.id
update_course_response = courses_client.update_course(course_id, update_course_request)
print(f'Изменеия курса по course_id: {course_id}:', update_course_response)

delete_course_request = courses_client.delete_course(course_id)
print(f'Удаление курса по сourse_id: {course_id}:', delete_course_request)
