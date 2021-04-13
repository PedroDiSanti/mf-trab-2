from bottle import Bottle, request

from marshmallow import ValidationError

from app.service.product import ProductService
from app.api.return_message import ReturnMessages

product_api = Bottle()
product_service = ProductService()


@product_api.post('/')
def create_product():
    payload = request.json
    if not payload:
        return ReturnMessages.error_payload()

    try:
        return ReturnMessages.success_create(product_service.create_product(payload))
    except ValidationError as schema_error:
        return ReturnMessages.error_field(schema_error)

