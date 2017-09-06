from flask import Flask, jsonify, Blueprint
from flasgger import Swagger


app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'PyVerde',
    'uiversion': 2
}

example_blueprint = Blueprint('example_blueprint', __name__, url_prefix='/lol')


@example_blueprint.route('/champion-mastery/v3/champion-masteries/by-summoner/<int:summonerId>', methods=['GET'])
def colors(summonerId):
    """
    aaa
    """
    return "OK"


app.register_blueprint(example_blueprint)

Swagger(app, template_file='swagger.json')