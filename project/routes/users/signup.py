from flask import Blueprint, render_template, request, session, redirect, url_for
import bcrypt
from project.routes.database import mongo
signup = Blueprint('signup', __name__)



@signup.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']}) #check if the username is in use
        if existing_user is None:
            password = request.form['password']
            users.insert({'name': request.form['username'], 'password': request.form['password']})
            session['username'] = request.form['username']
            return redirect(url_for('list_events'))
        return 'That username already exists! Try logging in.'
    return render_template('signup.html')
