from flask import redirect, url_for, render_template, Blueprint, request

home_blueprint = Blueprint('home', __name__)
indicators_count = 3

@home_blueprint.route('/', methods = ['GET'])
def index():
    return render_template("index.html", indicators_count=indicators_count)
    