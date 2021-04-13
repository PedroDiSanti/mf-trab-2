import uuid
from datetime import datetime

from marshmallow import Schema
from marshmallow.validate import Length
from marshmallow.fields import UUID, String, DateTime, Email

from app.utils.constants import DATETIME_FORMAT


class Customer(Schema):
    class Meta:
        ordered = True

    _id = UUID(required=False, allow_none=False, missing=uuid.uuid4)
    name = String(required=True, description='Nome do cliente.', validate=Length(min=1, max=100))
    email = Email(required=True, description='Email do client')
    password = String(required=True, description='Senha do cliente.', validate=Length(min=1, max=100))
    document = String(required=True, description='Documento do cliente.', validate=Length(min=1, max=100))
    created_at = DateTime(required=False, allow_none=True, description='Criado em.', missing=datetime.now,
                          format=DATETIME_FORMAT)
    updated_at = DateTime(required=False, allow_none=True, description='Atualizado em.', format=DATETIME_FORMAT)
