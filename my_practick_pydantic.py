from pydantic import BaseModel, SerializeAsAny

class ErrorDetails(BaseModel):
    code: int
    message: str
    message_en: str

class ErrorResponse(BaseModel):
    error: SerializeAsAny[ErrorDetails]

# Пример использования
error_response = {
    "error": {
        "code": 2030,
        "message": "Исчерпан лимит активаций промокода",
        "message2": "Исчерпан лимит активаций промокода",
        "message_en": "Promo code activation limit reached"
    }
}

response = ErrorResponse(**error_response)
print(response.model_dump())

class Confirmation(BaseModel):
    type: str
    return_url: str

class Customer(BaseModel):
    phone: str

class Payment(BaseModel):
    payment_token: str
    save_payment_method: bool
    confirmation: Confirmation
    customer: Customer

class Result(BaseModel):
    code: str
    shop: str
    payment: Payment
    clientType: str
    analyticServiceHash: str

class PromoSchema(BaseModel):
    result: Result


valid_respone = {
    "result": {
        "code": "aboba322",
        "shop": "123456",
        "payment": {
            "payment_token": "random aboba",
            "save_payment_method": True,
            "confirmation": {
                "type": "redirect",
                "return_url": "https://rc-v-stage-1706.k8s-01.prem-dev.env.zxz.su/profile/promocode?check=31xebyrb"
            },
            "customer": {
                "phone": "80000000"
            }
        },
        "clientType": "WEB",
        "analyticServiceHash": "123131231"
    }
}

valid_respone2 = PromoSchema(**valid_respone)
print(valid_respone2.model_dump())
