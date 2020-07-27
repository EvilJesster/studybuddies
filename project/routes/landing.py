from flask import Blueprint, render_template, session
from project import mongo
landing = Blueprint('landing', __name__)


@landing.route('/')
def tester():
   # userinfo = mongo.db.userinfo
    #userinfo.insert({'event': 'event_name', 'date': 'event_date', 'user': 'user_name'})
    if(session.get('lin') == True):
        return('magic')
    else:
        return(render_template('notloggedin.html'))
    return(render_template('base.html'))
