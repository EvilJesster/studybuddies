from flask import Blueprint, render_template, request,session
from project import mongo
users = mongo.db.users
foll = mongo.db.followlist
posts = mongo.db.posts

def grabposts():#filt,)
    pass
        #
        # posthold = []
        # if(posts.find_one(filt) != None):
        #     posthold = posts.find_one({'unique': session.get('unique')})['plist']