from flask import Blueprint, render_template, request,session, redirect, url_for
from project import mongo

users = mongo.db.users
foll = mongo.db.followlist
posts = mongo.db.posts

def isSetup(): #checks if a user has setup their account
    holder = users.find_one({'unique': session.get('unique')})
    if (holder['name'] == None):
        return (redirect(url_for('user.setup')))


