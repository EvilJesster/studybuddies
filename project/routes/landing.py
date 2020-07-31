from flask import Blueprint, render_template, session, redirect, url_for, request
from project.routes.users.forms import PostForm
from project.routes.users.models import User
from project import mongo
from datetime import datetime
landing = Blueprint('landing', __name__)
users = mongo.db.users
foll = mongo.db.followlist
posts = mongo.db.posts

@landing.route('/', methods=['POST', 'GET'])
def tester(): #TODO:make this a real name
    global users, foll, posts
    form = PostForm(request.form)
    #userinfo.insert({'event': 'event_name', 'date': 'event_date', 'user': 'user_name'})
    if(session.get('lin') == True):
        # make a post on feed
        if (request.method == 'POST' and form.validate()):
            holder = form.data['post']
            User.addpost(session.get('unique'), holder)
            return(redirect(url_for('landing.tester')))

        holder = users.find_one({'unique': session.get('unique')})
        if(holder['name'] == None):
            return(redirect(url_for('user.setup')))
        ready = True
        filt = {'unique': session.get('unique')}
        folhold = []
        if (foll.find_one(filt) != None):
            folhold = foll.find_one({'unique': session.get('unique')})['followlist']
        post = []
        folhold.append(session.get('username'))
        for i in folhold:
            posthold = {}
            if (posts.find_one({'username': i}) != None):
                posthold['post'] = posts.find_one({'username': i})['plist'][-1]
                curuse = users.find_one({'username':i})
                posthold['pfp'] = curuse['pfp']
                posthold['username'] = curuse['username']
                posthold['name'] = curuse['name']
                post.append(posthold)

        return(render_template('loggedin.html', info = holder, ready=ready, post=post, form=form, time=datetime.now()))

    else:
        return(render_template('notloggedin.html', time = datetime.now()))


@landing.route('/about')
def about():
    return(render_template('about.html', time = datetime.now()))

@landing.route('/subjects')
def subjects():
    return(render_template('subjects.html', time = datetime.now()))