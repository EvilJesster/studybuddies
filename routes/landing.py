from flask import Blueprint, render_template
from .database import mongo

landing = Blueprint('landing', __name__)


@landing.route('/')
def tester():
    #userinfo = mongo.db.userinfo
    #userinfo.insert({'event': 'event_name', 'date': 'event_date', 'user': 'user_name'})
    return(render_template('base.html'))
