from flask import Flask
from routes.database import mongo
from routes.landing import landing

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('Studybuddies-private')
app.debug = True
#app.config.from_pyfile('Studybuddies-private/config.py')
app. register_blueprint(landing)
mongo.init_app(app)