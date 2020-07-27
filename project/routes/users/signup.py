from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from project.routes.users.forms import UserForm
from project.routes.users.models import User

from project import mongo
signup = Blueprint('signup', __name__)



@signup.route('/signup', methods=['POST', 'GET'])
def signupp():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']}) #check if the username is in use
        if existing_user is None:
            new_user = User(form.data['username'], form.data['password'])
            new_user.pushdb()
            session['username'] = form.data['username'] #in theory should eventually make this secur
            return redirect(url_for('landing.tester'))
        flash( 'That username already exists! Try logging in.')
        return(redirect(url_for('login')))
    return render_template('signup.html', form=form)
