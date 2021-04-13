from marshmallow import ValidationError
from pymongo import MongoClient

from app.schema.customer import Customer


class CustomerService:
    def __init__(self):
        self.schema = Customer()

        self.mongodb_uri = 'localhost:27017'
        self.mongodb_name = 'Store'
        self.mongodb_collection = 'customer'

        self.db_connection = MongoClient(self.mongodb_uri).get_database(self.mongodb_name).get_collection(
            self.mongodb_collection)

    def create_customer(self, payload):
        try:
            data = self.schema.load(payload)
        except ValidationError as validation_error:
            raise validation_error
        created_id = self.db_connection.insert_one(data).inserted_id
        return created_id

    def get_customer_login(self, login, password):
        customer = self.db_connection.find_one({'$and': [{'email': login}, {'password': password}]})
        if customer:
            return self.schema.dump(customer)
        raise FileNotFoundError()

    def get_if_customer_exists(self, customer):
        customer = self.db_connection.find_one(
            {'$or': [{'email': customer.get('email')}, {'document': customer.get('document')}]})
        return True if customer else False
