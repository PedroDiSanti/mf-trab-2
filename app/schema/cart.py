import uuid
from datetime import datetime

from marshmallow import Schema
from marshmallow.fields import UUID, DateTime, Nested, List

from app.schema.product import Product
from app.utils.constants import DATETIME_FORMAT


class Cart(Schema):
    class Meta:
        ordered = True

    _id = UUID(required=False, allow_none=False, missing=uuid.uuid4)
    products = List(Nested(Product()), required=False, missing=[])
    customer_id = UUID(required=True)
    created_at = DateTime(required=False, allow_none=True, description='Criado em.', missing=datetime.now,
                          format=DATETIME_FORMAT)
    updated_at = DateTime(required=False, allow_none=True, description='Atualizado em.', format=DATETIME_FORMAT)
