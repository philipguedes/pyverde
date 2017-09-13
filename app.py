from flask import Flask, jsonify, Blueprint
from flasgger import Swagger
from pyverde.endpoints.champion_mastery import champion_mastery
from pyverde.endpoints.champion import champion
from pyverde.endpoints.league import league
from pyverde.endpoints.masteries import masteries
from pyverde.endpoints.match import match
from pyverde.endpoints.runes import runes
from pyverde.endpoints.spectator import spectator
from pyverde.endpoints.summoner import summoner


app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'PyVerde',
    'uiversion': 2
}


app.register_blueprint(champion_mastery)
app.register_blueprint(champion)
app.register_blueprint(league)
app.register_blueprint(masteries)
app.register_blueprint(match)
app.register_blueprint(runes)
app.register_blueprint(spectator)
app.register_blueprint(summoner)

Swagger(app, template_file='swagger.json')