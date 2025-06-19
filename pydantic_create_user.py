from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel

# Необходимо реализовать следующие модели:
#  UserSchema — модель данных пользователя ✔
#  CreateUserRequestSchema — запрос на создание пользователя ✔
#  CreateUserResponseSchema — ответ с данными созданного пользователя ✔

# Применить все лучшие практики
#  Применил только: Автоматическое преобразование snake_case → camelCase
#  get_username
#  Тк у нас в основном статические данные  И  три способа создания Pydantic-модели. Каждый из них > > удобен в разных ситуациях < <:
# думаю что в данной ситуациии с минимальными полями удобна эта реализация

# Требования к коду:
#  Читаемость и структурированность.  ✔
#  Соблюдение стандартов аннотации типов. ✔
#  Корректное именование моделей. ✔
#  Обязательное документирование кода с помощью docstring. ✔


#UserSchema — модель данных пользователя
class UserSchema(BaseModel):
    """
       Базовая модель данных пользователя

       Конфигурация:
        - Автоматическое преобразование имен полей из snake_case в camelCase

       Атрибуты:
           id (str): Уникальный идентификатор пользователя
           email (EmailStr): Электронная почта пользователя
           last_name (str): Фамилия пользователя
           first_name (str): Имя пользователя
           middle_name (str): Отчество пользователя
       """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


user_response = {
    "id": "12",
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

user_request = UserSchema(**user_response)
print(user_request.id)
print(user_request.model_dump(by_alias=True))


#CreateUserRequestSchema — запрос на создание пользователя
class CreateUserRequestSchema(BaseModel):
    """
        Запрос на создание нового пользователя

        Конфигурация:
        - Автоматическое преобразование имен полей из snake_case в camelCase

        Атрибуты:
            email (EmailStr): Электронная почта пользователя
            password (str): Пароль пользователя
            last_name (str): Фамилия пользователя
            first_name (str): Имя пользователя
            middle_name (str): Отчество пользователя

        Пример:
            {
                "email": "user@example.com",
                "password": "string",
                "lastName": "string",
                "firstName": "string",
                "middleName": "string"
            }
        """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str


create_user_request = {
    "email": "user@example.com",
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = CreateUserRequestSchema(**create_user_request)
print(create_user_response.model_dump(by_alias=True))


#class User(BaseModel):
#id: str
#email: EmailStr  # Используем EmailStr вместо str
#last_name: str = Field(alias="lastName")
#first_name: str = Field(alias="firstName")
#middle_name: str = Field(alias="middleName")

#CreateUserResponseSchema — ответ с данными созданного пользователя
class CreateUserResponseSchema(BaseModel):
    """
       Ответ содержащий данные созданного пользователя

       Конфигурация:
        - Автоматическое преобразование имен полей из snake_case в camelCase

       Атрибуты:
           user (UserSchema): Объект с данными созданного пользователя

       Пример:
           {
               "user": {
                   "id": "123",
                   "email": "user@example.com",
                   "lastName": "string",
                   "firstName": "string",
                   "middleName": "string"
               }
           }
       """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    user: UserSchema  # Не до конца понял как правильно
    # #Сделать новую схему которая выше или унаследовать от UserSchema


user_request = {
    "user": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
}

user_response = CreateUserResponseSchema(**user_request)
print(user_response.model_dump(by_alias=True))

