import os

from bottle import Bottle


from app.api.cart import cart_api
from app.api.product import product_api
from app.api.customer import customer_api

App = Bottle()

App.mount('/cart', cart_api)
App.mount('/product', product_api)
App.mount('/customer', customer_api)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    App.run(host='0.0.0.0', port=port, debug=True, reloader=True)
