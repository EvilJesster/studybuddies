from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from project.routes.users.forms import UserForm, SetupForm, SearchForm, PfpForm, PostForm
from project.routes.users.models import User
from project.routes.users.helper import isSetup
from datetime import datetime
from project import mongo
tools = Blueprint('tools', __name__)

#TODO: move search here

#TODO: put messaging here

