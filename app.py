#!/usr/bin/env python3


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.country import Country
from resources.state import State
from os import environ

DB_URL = environ["DB_URL"]
DB_USER = environ["DB_USER"]
DB_PASSWORD = environ["DB_PASSWORD"]
DB_NAME = environ["DB_NAME"]

DB_URI = 'mysql://{user}:{pw}@{url}/{db}'.format(user=DB_USER,pw=DB_PASSWORD,url=DB_URL,db=DB_NAME)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Country, '/country/<string:name>')
api.add_resource(State, '/state/<string:country>/<string:name>')

if __name__ == '__main__':
    app.run(port=5002, debug=True)
