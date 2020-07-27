from flask import Flask
from flask_bcrypt import Bcrypt
from project.routes.database import mongo



app = Flask(__name__, instance_relative_config=True)

#app.config.from_object('Studybuddies-private') pycharm was misbehaving, may revert to this structure eventually
app.debug = True
app.config.from_pyfile('config.py')

mongo.init_app(app)
bcrypt = Bcrypt(app)

from project.routes.landing import landing
app.register_blueprint(landing)

