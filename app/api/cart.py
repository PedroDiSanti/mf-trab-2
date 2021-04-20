from bottle import Bottle, request
from marshmallow import ValidationError

from app.service.cart import CartService
from app.api.customer import CustomerService
from app.service.product import ProductService

from app.api.return_message import ReturnMessages
from app.utils.validate_uuid import validate_if_uuid

cart_api = Bottle()
cart_service = CartService()
product_service = ProductService()
customer_service = CustomerService()


@cart_api.put('/<product_id>')
def add_product(product_id):
    login, password = request.auth
    customer = customer_service.get_customer_login(login, password)
    if not customer:
        return ReturnMessages.error_invalid_user_session()

    if not validate_if_uuid(product_id):
        return ReturnMessages.error_payload()

    product = product_service.get_product(product_id)
    if not product:
        return ReturnMessages.error_get_product()

    try:
        cart_service.add_product_to_cart(customer, product)
        return ReturnMessages.success_put()
    except ValidationError as schema_error:
        return ReturnMessages.error_field(schema_error)
    except FileNotFoundError:
        return ReturnMessages.error_get_cart()


@cart_api.delete('/<product_id>')
def remove_product(product_id):
    login, password = request.auth
    customer = customer_service.get_customer_login(login, password)
    if not customer:
        return ReturnMessages.error_invalid_user_session()

    if not validate_if_uuid(product_id):
        return ReturnMessages.error_payload()

    product = product_service.get_product(product_id)
    if not product:
        return ReturnMessages.error_get_product()

    try:
        cart_service.remove_product_from_cart(customer, product)
        return ReturnMessages.success_put()
    except ValidationError as schema_error:
        return ReturnMessages.error_field(schema_error)
    except FileNotFoundError:
        return ReturnMessages.error_get_cart()


