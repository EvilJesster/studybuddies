from flask import Flask
from flask_bcrypt import Bcrypt

from flask_pymongo import PyMongo
import os
is_prod = os.environ.get('IS_HEROKU', None)

app = Flask(__name__, instance_relative_config=True)

#app.config.from_object('Studybuddies-private') pycharm was misbehaving, may revert to this structure eventually
if(not is_prod):
    app.debug = True
    app.config.from_pyfile('newconfig.py')
mongo = PyMongo(app)

bcrypt = Bcrypt(app)

from project.routes.landing import landing
app.register_blueprint(landing)

from project.routes.users.user import user
app.register_blueprint(user)
