from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #sqlalchemy database lives in the root folder of the project
#app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turns of flask SQLAlchemy modification tracker but does not turn off SQLAlchemy modification tracker.
app.secret_key = 'michael'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

#app.config['JWT_AUTH_URL_RULE'] = '/login' #change Authentication URL
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) #config JWT to expire within half an hour

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
