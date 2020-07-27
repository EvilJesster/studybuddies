from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from project.routes.users.forms import UserForm, InfoForm
from project.routes.users.models import User
import uuid
from project import mongo
user = Blueprint('user', __name__)

users = mongo.db.users

@user.route('/signup', methods=['POST', 'GET'])
def signup():
    global users
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        existing_user = users.find_one({'username': request.form['username']}) #check if the username is in use
        if existing_user is None:
            holdunique = uuid.uuid4().hex
            new_user = User(form.data['username'], form.data['password'], holdunique)
            new_user.pushdb()
            session['username'] = form.data['username'] #TODO: secure sessions
            session['unique'] = holdunique
            session['lin'] = True
            return redirect(url_for('landing.tester'))
        flash( 'That username already exists! Try logging in.')
        return(redirect(url_for('user.login')))
    return render_template('signup.html', form=form)



@user.route('/login', methods=['GET', 'POST'])
def login():
    global users
    form = UserForm(request.form)
    if(request.method == 'POST' and form.validate()):
        if(User.authenticate(form.data['username'], form.data['password'])):
            session['username'] = form.data['username'] #TODO: secure sessions, maybe use unique id for this?

            temphold =  users.find_one({'username': form.data['username']})
            session['unique'] = temphold['unique']
            session['lin'] = True
            return(redirect(url_for('landing.tester')))
        flash('invalid username or password')
        return redirect(url_for('user.login'))
        #TODO: return to this and fix it so it properly sends you to sign up n stuff
    return render_template('login.html', form=form)


@user.route('/setup', methods=['GET', 'POST'])
def setup():
    global users
    form = InfoForm(request.form)
    if(request.method =='POST' and form.validate()):
        holder = users.find_one({'unique': session.get('unique')})
        User.addmore(session.get('unique'), form.data)
        return(redirect(url_for('landing.tester')))
    return(render_template('setup.html', form=form))

@user.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landing.tester'))
