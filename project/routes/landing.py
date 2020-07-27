from flask import Blueprint, render_template, session
from project import mongo
landing = Blueprint('landing', __name__)


@landing.route('/')
def tester():
    users = mongo.db.users
    #userinfo.insert({'event': 'event_name', 'date': 'event_date', 'user': 'user_name'})
    if(session.get('lin') == True):
        holder = users.find_one({'unique': session.get('unique') })
        if(holder['name'] == None):
            return('yeet')
        return('magic')
    else:
        return(render_template('notloggedin.html'))
    return(render_template('base.html'))
