from flask import Blueprint, render_template
from .database import mongo
login = Blueprint('login', __name__)



@login.route('/login', methods=['GET', 'POST'])

def login():
    users = mongo.db.userinfo
    login_user = users.find_one({'name' : request.form['username']})
    if login_user:
        if request.form['password'] == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('mainpage'))
        return redirect(url_for('index'))
    return render_template('signup.html') 