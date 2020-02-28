from flask import Flask
from flask_restful import Resource,Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

students = []

jwt = JWT(app, authenticate, identity)

#these are the routes like @app.route("/")
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=true)