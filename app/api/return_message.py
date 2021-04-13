import json

from bottle import HTTPResponse

from app.utils.constants import HEADERS_RESPONSE


class ReturnMessages:
    @classmethod
    def success_create(cls, created_id):
        return HTTPResponse({'created_id': str(created_id)}, 201, HEADERS_RESPONSE)

    @classmethod
    def success_get_memo(cls, result_object):
        return HTTPResponse(result_object, 200, HEADERS_RESPONSE)

    @classmethod
    def success_delete_memo(cls):
        return HTTPResponse(json.dumps({"Message": "The memo was deleted."}), 200, HEADERS_RESPONSE)

    @classmethod
    def error_payload(cls):
        return HTTPResponse(json.dumps({"Error": "Invalid Payload."}), 422, HEADERS_RESPONSE)

    @classmethod
    def error_validation_uuid(cls):
        return HTTPResponse(json.dumps({"Error": "Invalid UUID."}), 422, HEADERS_RESPONSE)

    @classmethod
    def error_get_memo(cls):
        raise HTTPResponse(json.dumps({"Error": "No memo was found."}), 404, HEADERS_RESPONSE)

    @classmethod
    def error_field(cls, error_validate_schema):
        return HTTPResponse(json.dumps({"Error": error_validate_schema.args}), 422, HEADERS_RESPONSE)

    @classmethod
    def error_invalid_user_session(cls):
        return HTTPResponse(json.dumps({"Error": "Invalid user session."}), 404, HEADERS_RESPONSE)

    @classmethod
    def error_delete_memo(cls):
        return HTTPResponse(json.dumps({"Error": "The memo was not deleted."}), 400, HEADERS_RESPONSE)
