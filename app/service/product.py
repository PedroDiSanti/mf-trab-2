import os
from uuid import UUID

from pymongo import MongoClient

from marshmallow import ValidationError

from app.schema.product import Product


class ProductService:
    def __init__(self):
        self.schema = Product()

        self.mongodb_uri = os.getenv('MONGODB_URI') if os.getenv('MONGODB_URI') else 'localhost:27017'
        self.mongodb_name = 'Store'
        self.mongodb_collection = 'product'

        self.db_connection = MongoClient(self.mongodb_uri).get_database(self.mongodb_name).get_collection(
            self.mongodb_collection)

    def create_product(self, payload):
        try:
            data = self.schema.load(payload)
            created_id = self.db_connection.insert_one(data).inserted_id
        except ValidationError as validation_error:
            raise validation_error
        return created_id

    def get_product(self, product_id):
        product = self.db_connection.find_one({'_id': UUID(product_id), 'enabled': True})
        if product:
            return self.schema.dump(product)
        raise FileNotFoundError()

    def get_all_products(self):
        products = self.db_connection.find({'enabled': True})
        if products:
            return self.schema.dumps(products, many=True)
        raise FileNotFoundError()
