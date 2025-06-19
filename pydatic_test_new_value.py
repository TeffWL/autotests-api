from pydantic import BaseModel, SerializeAsAny


class ErrorDetails(BaseModel):
    code: int
    message: str
    message_en: str

    class Config:
        extra = 'forbid'


class ErrorResponse(BaseModel):
    error: SerializeAsAny[ErrorDetails]


# Пример использования
error_response = {
    "error": {
        "code": 2030,
        "message": "Исчерпан лимит активаций промокода",
        "message_eu": "Лишний параметр приходит",
        "message_en": "Promo code activation limit reached"

}
}
response = ErrorResponse(**error_response)
print(response.model_dump())
