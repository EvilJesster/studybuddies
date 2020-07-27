from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from project.routes.users.forms import UserForm
from project.routes.users.models import User

from project import mongo
user = Blueprint('user', __name__)



@user.route('/signup', methods=['POST', 'GET'])
def signup():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']}) #check if the username is in use
        if existing_user is None:
            new_user = User(form.data['username'], form.data['password'])
            new_user.pushdb()
            session['username'] = form.data['username'] #TODO: secure sessions
            session['lin'] = True
            return redirect(url_for('landing.tester'))
        flash( 'That username already exists! Try logging in.')
        return(redirect(url_for('user.login')))
    return render_template('signup.html', form=form)



@user.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm(request.form)
    if(request.method == 'POST' and form.validate()):
        if(User.authenticate(form.data['username'], form.data['password'])):
            session['username'] = form.data['username'] #TODO: secure sessions, maybe use unique mongo id for this?
            session['lin'] = True
            return(redirect(url_for('landing.tester')))
        flash('invalid username or password')
        return redirect(url_for('user.login'))
        #TODO: return to this and fix it so it properly sends you to sign up n stuff
    return render_template('login.html', form=form)


