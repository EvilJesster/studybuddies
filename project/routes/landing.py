from flask import Blueprint, render_template, session, redirect, url_for
from project import mongo
landing = Blueprint('landing', __name__)


@landing.route('/')
def tester():
    users = mongo.db.users
    #userinfo.insert({'event': 'event_name', 'date': 'event_date', 'user': 'user_name'})
    if(session.get('lin') == True):
        holder = users.find_one({'unique': session.get('unique')})
        if(holder['name'] == None):
            return(redirect(url_for('user.setup')))
        return(render_template('loggedin.html'))
    else:
        return(render_template('notloggedin.html'))
    return(render_template('base.html'))
