from flask import redirect, url_for, render_template, Blueprint, request

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods = ['GET'])
def index():
    return render_template("index.html")
    