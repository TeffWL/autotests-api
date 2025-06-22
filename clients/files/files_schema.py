from pydantic import BaseModel, HttpUrl, ConfigDict
from pydantic.alias_generators import to_camel


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
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema
