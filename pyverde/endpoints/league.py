from flask import Blueprint, request


__prefix = '/lol/league/v3'
league = Blueprint('league', __name__, url_prefix=__prefix)


# TODO: Custom validator to check if queue is in RANKED_* format
@league.route('/challengerleagues/by-queue/<string:queue>', methods=['GET'])
def get_challenger_league_by_queue(queue):
    return "OK"


@league.route('/leagues/by-summoner/<int:summonerId>', methods=['GET'])
def get_leagues_by_summoner(summonerId):
    return "OK"


@league.route('/masterleagues/by-queue/<string:queue>', methods=['GET'])
def get_master_league_by_queue(queue):
    return "OK"


@league.route('/positions/by-summoner/<int:summonerId>', methods=['GET'])
def get_leagues_position_by_summoner(summonerId):
    return "OK"