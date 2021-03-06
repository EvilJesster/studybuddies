from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from project.routes.users.forms import UserForm, SetupForm, SearchForm, PfpForm, PostForm
from project.routes.users.models import User
from project.routes.users.helper import isSetup
from datetime import datetime
import uuid, json
from project import mongo
user = Blueprint('user', __name__)

users = mongo.db.users
foll = mongo.db.followlist
posts = mongo.db.posts


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
    # if(request.method=='POST'):
    #     print(form.data)
    #     print(form.validate())
    #     print(form.errors)
    if (session.get('lin') == True):
        if(request.method =='POST' and form.validate()):
            holder = users.find_one({'unique': session.get('unique')})
            User.addmore(session.get('unique'), form.data)
            return(redirect(url_for('landing.tester')))
        return(render_template('setup.html', form=form, time = datetime.now()))
    return(redirect(url_for('landing.tester')))




@user.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landing.tester'))

@user.route('/profile', methods = ['GET', 'POST'])
def profile():
    global users
    global foll
    global posts
    form = PostForm(request.form)
    if (session.get('lin') == True):
        if (request.method == 'POST' and form.validate()):
            holder = form.data['post']
            User.addpost(session.get('unique'), holder)
            return(redirect(url_for('user.profile')))
        uinfo = users.find_one({'unique': session.get('unique')})
        if (uinfo['name'] == None):
            return (redirect(url_for('user.setup')))
        ownpro = True
        filt = {'unique':  session.get('unique')}
        posthold = []
        if(posts.find_one(filt) != None):
            posthold = posts.find_one({'unique': session.get('unique')})['plist'][::-1]
        #TODO: add way to remove a strength or weakness
        return(render_template('profile.html', info=uinfo, ownpro = ownpro, form=form, posts=posthold,  time = datetime.now()))
    return(redirect(url_for('landing.tester')))



@user.route('/search', methods = ['GET', 'POST'])
def search(): #TODO: move to tools
    global users
    form = SearchForm(request.form)
    if(session.get('lin') == True):
        isSetup()
        if (request.method == 'POST' and form.validate()):
            #display user in order of matches with search
            print(form.data)
            results = []
            if(form.data['uname'] != ''):

                pfound = users.find_one({'username': form.data['uname']})
                if(pfound != None):
                    if(pfound['name'] != None):
                        results = [[pfound, 90]]
                if(results == []):
                    return (render_template('search.html', form=form, time=datetime.now()))
            else:
                filt = {'name':{'$ne': None}}
                udump = users.find(filt)
                print(type(udump))
                smatcount = {} #holds the matches counter for results
                for i in udump:
                    smatcount[i['_id']] = []
                    smatcount[i['_id']].append(0)
                    smatcount[i['_id']][0] += len(set(i['art']['strengths']) & set(form.data['art']['strengths']))
                    smatcount[i['_id']][0] += len(set(i['art']['weaknesses']) & set(form.data['art']['weaknesses']))
                    smatcount[i['_id']][0] += len(set(i['business']['strengths']) & set(form.data['business']['strengths']))
                    smatcount[i['_id']][0] += len(set(i['business']['weaknesses']) & set(form.data['business']['weaknesses']))
                    smatcount[i['_id']][0] += len(set(i['engineering']['strengths']) & set(form.data['engineering']['strengths']))
                    smatcount[i['_id']][0] += len(set(i['engineering']['weaknesses']) & set(form.data['engineering']['weaknesses']))
                    smatcount[i['_id']][0] += len(set(i['humanities']['strengths']) & set(form.data['humanities']['strengths']))
                    smatcount[i['_id']][0] += len(set(i['humanities']['weaknesses']) & set(form.data['humanities']['weaknesses']))
                    smatcount[i['_id']][0] += len(set(i['math']['strengths']) & set(form.data['math']['strengths']))
                    smatcount[i['_id']][0] += len(set(i['math']['weaknesses']) & set(form.data['math']['weaknesses']))
                print(smatcount)
                results = []
                for key, value in smatcount.items():
                    if (value[0] >= 1):
                        results.append([users.find_one({'_id': key}), value])
            return(render_template('search.html', form=form, time=datetime.now(), results=results))
                    
        return(render_template('search.html', form=form, time=datetime.now()))
    return(redirect(url_for('user.login')))


@user.route('/changepfp', methods=['GET', 'POST'])
def changepfp():
    form = PfpForm(request.form)
    if (session.get('lin') == True):
        if (request.method == 'POST' and form.validate()):
            User.addpfp(form.data['pfp'], session.get('unique'))
            return(redirect(url_for('user.profile')))
        return render_template('updatepfp.html', form=form, time=datetime.now())
    return(redirect(url_for('landing.tester')))


@user.route('/<page>', methods=['GET', 'POST'])
def other(page):
    global users
    global foll
    if (session.get('lin') == True):
        if (request.method == 'POST'):
            print(request.form['follow'])
            User.follow(session.get('unique'), page)
        isSetup()
        selected = users.find_one({'username': page})
        folhold = foll.find_one({'unique': session.get('unique')})['followlist']
        ownpro = False
        isfol = False
        if(page in folhold):
            isfol = True
        posthold = []
        if (posts.find_one({'username': page}) != None):
            posthold = posts.find_one({'username': page})['plist'][::-1]
        return(render_template('profile.html', info =selected, ownpro = ownpro, isfol=isfol, posts=posthold, time=datetime.now()))
    return (redirect(url_for('landing.tester')))

@user.route('/following')
def following():
    global foll
    global users
    if(session.get('lin') == True):
        isSetup()
        filt = {'unique': session.get('unique')}
        folhold = []
        if (foll.find_one(filt) != None):
            folhold = foll.find_one({'unique': session.get('unique')})['followlist']
        return(render_template('following.html', following=folhold, time=datetime.now()))
    return (redirect(url_for('landing.tester')))


@user.route('/messaging', methods=['GET', 'POST'])
def messaging():
    if (session.get('lin') == True):
        isSetup()
        return(render_template('messaging.html'))
    return (redirect(url_for('landing.tester')))


@user.route('/messagingback', methods=['POST']) #todo: move this to tools
def snedmess():
    sender = request.form['message']
    return(json.dumps({' status': 'OK', 'message': sender}))




