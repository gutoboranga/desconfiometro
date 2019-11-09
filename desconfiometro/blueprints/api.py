from flask import redirect, url_for, render_template, Blueprint, request

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api', methods = ['GET'])
def get():
    return ("AAA")
    