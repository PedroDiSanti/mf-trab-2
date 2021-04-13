import os

from bottle import Bottle


from app.api.cart import cart_api
from app.api.product import product_api
from app.api.customer import customer_api

App = Bottle()

App.mount('/cart', cart_api)
App.mount('/product', product_api)
App.mount('/customer', customer_api)


if os.environ.get('APP_LOCATION') == 'heroku':
    App.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True, reloader=True)
else:
    App.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
