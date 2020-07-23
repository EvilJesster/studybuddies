from flask import Flask
from flask_pymongo import PyMongo
from routes.landing import landing

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('Studybuddies-private')
#app.config.from_pyfile('config.py')
app. register_blueprint(landing)
mongo = PyMongo(app)
# @app.route('/')
# def index():
#     collection = mongo.db.userinfo
#     return('hello')
