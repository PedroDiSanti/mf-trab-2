import uuid
from datetime import datetime

from marshmallow import Schema
from marshmallow.validate import Length
from marshmallow.fields import UUID, String, DateTime, Bool, Float

from app.utils.constants import DATETIME_FORMAT


class Product(Schema):
    class Meta:
        ordered = True

    _id = UUID(required=False, allow_none=False, missing=uuid.uuid4)
    name = String(required=True, description='Nome do produto.', validate=Length(min=1, max=1000))
    description = String(required=True, description='Descrição do produto.', validate=Length(min=1, max=1000))
    price = Float(required=True, description='Valor do produto.')
    enabled = Bool(required=False, description='Se o produto está ativado ou desativado.', missing=True)
    created_at = DateTime(required=False, allow_none=True, description='Criado em.', missing=datetime.now,
                          format=DATETIME_FORMAT)
    updated_at = DateTime(required=False, allow_none=True, description='Atualizado em.', format=DATETIME_FORMAT)
    deleted_at = DateTime(required=False, allow_none=True, description='Deletado em.', format=DATETIME_FORMAT)
