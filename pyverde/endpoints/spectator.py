import requests
from flask import Blueprint, request
from pyverde.decorators import make_request


__prefix = '/lol/spectator/v3'
spectator = Blueprint('spectator', __name__, url_prefix=__prefix)


@spectator.route('/active-games/by-summoner/<int:summonerId>', methods=['GET'])
@make_request(request)
def get_active_game_information(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@spectator.route('/featured-games')
@make_request(request)
def get_featured_games(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response
