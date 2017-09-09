from flask import Blueprint, request


__prefix = '/lol/spectator/v3'
spectator = Blueprint('spectator', __name__, url_prefix=__prefix)


@spectator.route('/active-games/by-summoner/<int:summonerId>', methods=['GET'])
def get_active_game_information(summonerId):
    return "OK"


@spectator.route('/featured-games')
def get_featured_games():
    return "OK"
