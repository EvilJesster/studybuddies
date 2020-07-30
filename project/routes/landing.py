from flask import Blueprint, render_template, session, redirect, url_for, request
from project.routes.users.forms import PostForm
from project.routes.users.models import User
from project import mongo
from datetime import datetime
landing = Blueprint('landing', __name__)
users = mongo.db.users
foll = mongo.db.followlist
posts = mongo.db.posts

@landing.route('/')
def tester(): #TODO:make this a real name
    global users,foll, posts
    form = PostForm(request.form)
    #userinfo.insert({'event': 'event_name', 'date': 'event_date', 'user': 'user_name'})
    if(session.get('lin') == True):
        holder = users.find_one({'unique': session.get('unique')})
        if(holder['name'] == None):
            return(redirect(url_for('user.setup')))
        ready = True
        filt = {'unique': session.get('unique')}
        folhold = []
        if (foll.find_one(filt) != None):
            folhold = foll.find_one({'unique': session.get('unique')})['followlist']
        post = []
        for i in folhold:
            posthold = {}
            if (posts.find_one({'username': i}) != None):
                posthold['post'] = posts.find_one({'username': i})['plist'][::-1]
                curuse = users.find_one({'username':i})
                posthold['pfp'] = curuse['pfp']
                posthold['username'] = curuse['username']
                posthold['name'] = curuse['name']
                post.append(posthold)

        return(render_template('loggedin.html', user = holder['name'], ready=ready, post=post, time=datetime.now()))
    else:
        return(render_template('notloggedin.html', time = datetime.now()))
    return(render_template('base.html', time = datetime.now()))

@landing.route('/about')
def about():
    return(render_template('about.html', time = datetime.now()))

@landing.route('/subjects')
def subjects():
    return(render_template('subjects.html', time = datetime.now()))