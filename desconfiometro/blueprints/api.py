from flask import redirect, url_for, render_template, Blueprint, request
from flask_cors import cross_origin
from urllib.parse import urlparse

from desconfiometro.blueprints.models.Analyzer import Analyzer
from desconfiometro.indicators.DNS import DNS
from desconfiometro.indicators.Greenlist import Greenlist
from desconfiometro.indicators.Certificate import Certificate
from desconfiometro.indicators.Redirects import Redirects
from desconfiometro.indicators.SpecialCharacters import SpecialCharacters
from desconfiometro.indicators.ReclameAqui import ReclameAqui


api_blueprint = Blueprint('api', __name__)
weighted_indicators = [ (Greenlist(), 0.2),
                        (Certificate(), 0.2),
                        (DNS(), 0.2),
                        (SpecialCharacters(), 0.2),
                        (Redirects(), 0.15),
                        (ReclameAqui(), 0.3)]
                        
analyzer = Analyzer(weighted_indicators)

@api_blueprint.route('/api', methods = ['GET'])
@cross_origin()
def get():
    parsed_url = urlparse(request.args['url'])
    
    analyzer.run(parsed_url)
    
    results = analyzer.getResults()
    score = analyzer.getScore()
    
    return render_template("result.html", results=results, score=score)
    