from bottle import Bottle, request
from marshmallow import ValidationError

from app.api.return_message import ReturnMessages
from app.service.cart import CartService
from app.service.customer import CustomerService

customer_api = Bottle()
customer_service = CustomerService()
cart_service = CartService()


@customer_api.post('/')
def create_customer():
    payload = request.json
    if not payload:
        return ReturnMessages.error_payload()

    customer_exists = customer_service.get_if_customer_exists(payload)
    if customer_exists:
        return ReturnMessages.error_payload()

    try:
        result = customer_service.create_customer(payload)
        cart_service.create_cart({'customer_id': result})
        return ReturnMessages.success_create(result)
    except ValidationError as schema_error:
        return ReturnMessages.error_field(schema_error)
