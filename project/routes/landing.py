from flask import Blueprint, render_template, session, redirect, url_for
from project import mongo
from datetime import datetime
landing = Blueprint('landing', __name__)


@landing.route('/')
def tester(): #TODO:make this a real name
    users = mongo.db.users
    #userinfo.insert({'event': 'event_name', 'date': 'event_date', 'user': 'user_name'})
    if(session.get('lin') == True):
        holder = users.find_one({'unique': session.get('unique')})
        if(holder['name'] == None):
            return(redirect(url_for('user.setup')))
        return(render_template('loggedin.html', user = holder['name']))
    else:
        return(render_template('notloggedin.html', time = datetime.now()))
    return(render_template('base.html', time = datetime.now()))
