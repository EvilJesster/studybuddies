from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from project.routes.users.forms import UserForm, SetupForm, SearchForm, MathForm, BusinessForm, ScienceForm, EngineeringForm, HumanitiesForm, ArtForm
from project.routes.users.models import User
from datetime import datetime
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
            holdunique = uuid.uuid4().hex  #generate unique identifier to misuse
            new_user = User(form.data['username'], form.data['password'], holdunique) #create user
            new_user.pushdb() #push user to db
            session['username'] = form.data['username'] #TODO: secure sessions
            session['unique'] = holdunique #currently using the unique id for "secure" sessions
            session['lin'] = True
            return redirect(url_for('landing.tester'))
        flash( 'That username already exists! Try logging in.')
        return(redirect(url_for('user.login')))
    return render_template('signup.html', form=form, time = datetime.now())



@user.route('/login', methods=['GET', 'POST'])
def login():
    global users
    form = UserForm(request.form)
    if (session.get('lin') == True):
        return(redirect(url_for('landing.tester')))
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
    return render_template('login.html', form=form, time = datetime.now())


@user.route('/setup', methods=['GET', 'POST'])
def setup():
    global users
    form = SetupForm(request.form)
    if(request.method=='POST'):
        print(form.data)
        print(form.validate())
        print(form.errors)
    if(request.method =='POST' and form.validate()):
        holder = users.find_one({'unique': session.get('unique')})
        User.addmore(session.get('unique'), form.data)
        return(redirect(url_for('landing.tester')))
    return(render_template('setup.html', form=form, time = datetime.now()))




@user.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landing.tester'))

@user.route('/profile')
def profile():
    global users
    if(session.get('lin') == True):
        holder = users.find_one({'unique': session.get('unique')})
        return(render_template('profile.html', info=holder, time = datetime.now()))

    return(redirect(url_for('landing.tester')))

@user.route('/search', methods = ['GET', 'POST'])
def search():
    global users
    form = SearchForm(request.form)
    if(session.get('lin') == True):
        if (request.method == 'POST' and form.validate()):
            #display user in order of matches with search
            print(form.data)
            if(form.data['uname'] != ''):
                pfound = users.find_one({'username': form.data['uname']})
            else:
                udump = users.find()
                print(type(udump))
                holder = {}
                for i in udump:
                    holder[i['_id']] = 0

                    holder[i['_id']] += len(set(i['art']['strengths']) & set(form.data['art']['strengths']))
                    holder[i['_id']] += len(set(i['art']['weaknesses']) & set(form.data['art']['weaknesses']))

                    holder[i['_id']] += len(set(i['business']['strengths']) & set(form.data['business']['strengths']))
                    holder[i['_id']] += len(set(i['business']['weaknesses']) & set(form.data['business']['weaknesses']))

                    holder[i['_id']] += len(set(i['engineering']['strengths']) & set(form.data['engineering']['strengths']))
                    holder[i['_id']] += len(set(i['engineering']['weaknesses']) & set(form.data['engineering']['weaknesses']))
                    holder[i['_id']] += len(set(i['humanities']['strengths']) & set(form.data['humanities']['strengths']))
                    holder[i['_id']] += len(set(i['humanities']['weaknesses']) & set(form.data['humanities']['weaknesses']))
                    holder[i['_id']] += len(set(i['math']['strengths']) & set(form.data['math']['strengths']))
                    holder[i['_id']] += len(set(i['math']['weaknesses']) & set(form.data['math']['weaknesses']))
                print(holder)

        return(render_template('search.html', form=form, time=datetime.now()))
    return(redirect(url_for('user.login')))


