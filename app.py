from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('Studybuddies-private')
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return('hello')
