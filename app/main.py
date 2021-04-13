from bottle import Bottle


from app.api.cart import cart_api
from app.api.product import product_api
from app.api.customer import customer_api

App = Bottle()

App.mount('/cart', cart_api)
App.mount('/product', product_api)
App.mount('/customer', customer_api)


if __name__ == '__main__':
    App.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
