import pydantic
from pydantic import BaseModel, HttpUrl, ConfigDict, Field
from pydantic.alias_generators import to_camel

from tools.fakers import fake


# GET /api/v1/files/{file_id}
# request x
# response  ✔ FileResponseSchema
# error  ✔ ValidationError

# POST /api/v1/files
# request ✔ CreateFileRequestSchema
# response  ✔ FileResponseSchema
# error  ✔ ValidationError

# DELTETE /api/v1/files/{file_id}

# Добавили описание структуры файла

class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    # Директорию оставляем статичной, чтобы все тестовые файлы на сервере попадали в одну папку
    directory: str = Field(default="tests")
    upload_file: pydantic.FilePath


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    Описание структуры запроса получения файла.
    """
    file: FileSchema
