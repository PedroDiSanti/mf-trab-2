import os
from uuid import UUID

from pymongo import MongoClient

from marshmallow import ValidationError

from app.schema.cart import Cart


class CartService:
    def __init__(self):
        self.schema = Cart()

        self.mongodb_uri = os.getenv('MONGODB_URI') if os.getenv('MONGODB_URI') else 'localhost:27017'
        self.mongodb_name = 'Store'
        self.mongodb_collection = 'cart'

        self.db_connection = MongoClient(self.mongodb_uri).get_database(self.mongodb_name).get_collection(
            self.mongodb_collection)

    def create_cart(self, payload):
        try:
            data = self.schema.load(payload)
            created_id = self.db_connection.insert_one(data).inserted_id
        except ValidationError as validation_error:
            raise validation_error
        return created_id

    def add_product_to_cart(self, customer, product):
        cart = self.db_connection.find_one({'customer_id': UUID(customer.get('_id'))})
        if not cart:
            raise FileNotFoundError

        try:
            self.db_connection.update_one({'_id': cart.get('_id')}, {"$push": {"products": product}})
        except ValidationError as validation_error:
            raise validation_error

    def remove_product_from_cart(self, customer, product):
        cart = self.db_connection.find_one({'customer_id': UUID(customer.get('_id'))})
        if not cart:
            raise FileNotFoundError

        result = self.db_connection.find_one({'_id': cart.get('_id')})
        if result.get('products'):
            result.get('products').pop(result.get('products').index(product))
        else:
            raise FileNotFoundError

        try:
            self.db_connection.update_one({'_id': cart.get('_id')}, {"$set": {"products": result.get('products')}})
        except ValidationError as validation_error:
            raise validation_error
