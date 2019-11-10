from flask import redirect, url_for, render_template, Blueprint, request
from flask_cors import cross_origin
from urllib.parse import urlparse

from desconfiometro.blueprints.models.Analyzer import Analyzer
from desconfiometro.indicators.DNS import DNS
from desconfiometro.indicators.Greenlist import Greenlist
from desconfiometro.indicators.Votes import Votes
from desconfiometro.indicators.Certificate import Certificate
from desconfiometro.indicators.Redirects import Redirects
from desconfiometro.indicators.SpecialCharacters import SpecialCharacters
from desconfiometro.indicators.ReclameAqui import ReclameAqui


api_blueprint = Blueprint('api', __name__)
weighted_indicators = [ (DNS(), 0.2),
                        (Votes(), 0.3),
                        (ReclameAqui(), 0.5),
                        (Greenlist(), 1.0),
                        (Certificate(), 0.5),
                        (SpecialCharacters(), 0.1),
                        (Redirects(), 0.15)]

analyzer = Analyzer(weighted_indicators)

@api_blueprint.route('/api', methods = ['GET'])
@cross_origin()
def get():
    url = request.args['url'] if 'http' in request.args['url'] else "https://" + request.args['url']
    parsed_url = urlparse(url)
    
    analyzer.run(parsed_url)
    
    results = analyzer.getResults()
    score = analyzer.getScore()
    color = get_color(score)

    return render_template("result.html", results=results, score=int(score * 10), color=color)
    
def get_color(score):
    if score <= 2:
        return "#D23838"
    if score <= 4:
        return "#F07D39"
    if score <= 6:
        return "#F0CA39"
    if score < 9:
        return "#7BC641"
    if score <= 10:
        return "#2CAE51"
    return "#FFFFFF"
       
