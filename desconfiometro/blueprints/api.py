from flask import redirect, url_for, render_template, Blueprint, request
from flask_cors import cross_origin
from urllib.parse import urlparse

from desconfiometro.blueprints.models.Analyzer import Analyzer
from desconfiometro.indicators.IP import IP
from desconfiometro.indicators.Greenlist import Greenlist
from desconfiometro.indicators.Certificate import Certificate
from desconfiometro.indicators.SpecialCharacters import SpecialCharacters


api_blueprint = Blueprint('api', __name__)
indicators = [Greenlist(), Certificate(), IP(), SpecialCharacters()]
analyzer = Analyzer(indicators)

@api_blueprint.route('/api', methods = ['GET'])
@cross_origin()
def get():
    parsed_url = urlparse(request.args['url'])
    results = analyzer.run(parsed_url)
    score = 8.0
    
    return render_template("result.html", results=results, score=score)
    