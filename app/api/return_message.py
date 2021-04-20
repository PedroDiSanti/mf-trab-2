import json

from bottle import HTTPResponse

from app.utils.constants import HEADERS_RESPONSE


class ReturnMessages:
    @classmethod
    def success_create(cls, created_id):
        return HTTPResponse({'created_id': str(created_id)}, 201, HEADERS_RESPONSE)

    @classmethod
    def success_get(cls, result_object):
        return HTTPResponse(result_object, 200, HEADERS_RESPONSE)

    @classmethod
    def success_list(cls, result_object):
        return HTTPResponse({"objects": json.loads(result_object)}, 200, HEADERS_RESPONSE)

    @classmethod
    def success_put(cls):
        return HTTPResponse({"Success": 'The cart was updated.'}, 200, HEADERS_RESPONSE)

    @classmethod
    def error_payload(cls):
        return HTTPResponse(json.dumps({"Error": "Invalid Payload."}), 422, HEADERS_RESPONSE)

    @classmethod
    def error_validation_uuid(cls):
        return HTTPResponse(json.dumps({"Error": "Invalid UUID."}), 422, HEADERS_RESPONSE)

    @classmethod
    def error_get_product(cls):
        raise HTTPResponse(json.dumps({"Error": "No product was found."}), 404, HEADERS_RESPONSE)

    @classmethod
    def error_get_cart(cls):
        raise HTTPResponse(json.dumps({"Error": "No cart was found."}), 404, HEADERS_RESPONSE)

    @classmethod
    def error_field(cls, error_validate_schema):
        return HTTPResponse(json.dumps({"Error": error_validate_schema.args}), 422, HEADERS_RESPONSE)

    @classmethod
    def error_invalid_user_session(cls):
        return HTTPResponse(json.dumps({"Error": "Invalid user session."}), 404, HEADERS_RESPONSE)
