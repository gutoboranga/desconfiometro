from flask import redirect, url_for, render_template, Blueprint, request
from flask_cors import cross_origin

api_blueprint = Blueprint('api', __name__)

class Result():
    
    def __init__(self, indicator_name, indicator_description, value, type):
        self.indicator_name = indicator_name
        self.indicator_description = indicator_description
        self.value = value
        self.type = type
        
results = [Result("Certificado", "Se o site tem o cadeadinho", 0, 'bool'), Result("Nota no reclame aqui", "Avaliação no site", 7.8, 'number')]
score = 5.7

@api_blueprint.route('/api', methods = ['GET'])
@cross_origin()
def get():
    html = render_template("result.html", results=results, score=score)
    return html
    