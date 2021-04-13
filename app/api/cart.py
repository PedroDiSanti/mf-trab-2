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


@cart_api.post('/<product_id>')
def add_product(product_id):
    login, password = request.auth
    customer = customer_service.get_customer_login(login, password)
    if not customer:
        return ReturnMessages.error_get_memo()

    if not validate_if_uuid(product_id):
        return ReturnMessages.error_payload()

    product = product_service.get_product(product_id)
    if not product:
        return ReturnMessages.error_get_memo()

    try:
        return ReturnMessages.success_create(cart_service.add_product_to_cart(customer, product))
    except ValidationError as schema_error:
        return ReturnMessages.error_field(schema_error)
    except FileNotFoundError:
        return ReturnMessages.error_delete_memo()


@cart_api.delete('/<product_id>')
def remove_product(product_id):
    login, password = request.auth
    customer = customer_service.get_customer_login(login, password)
    if not customer:
        return ReturnMessages.error_get_memo()

    if not validate_if_uuid(product_id):
        return ReturnMessages.error_payload()

    product = product_service.get_product(product_id)
    if not product:
        return ReturnMessages.error_get_memo()

    try:
        return ReturnMessages.success_create(cart_service.remove_product_to_cart(customer, product))
    except ValidationError as schema_error:
        return ReturnMessages.error_field(schema_error)
    except FileNotFoundError:
        return ReturnMessages.error_delete_memo()


