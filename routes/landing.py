from flask import Blueprint, render_template

landing = Blueprint('landing', __name__)
@landing.route('/')
def tester():
    return('hell')