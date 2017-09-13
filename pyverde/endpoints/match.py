import requests
from flask import Blueprint, request
from pyverde.decorators import make_request


__prefix = '/lol/match/v3'
match = Blueprint('match', __name__, url_prefix=__prefix)


@match.route('/matches/by-tournament-code/<string:tournamentCode>/ids', methods=['GET'])
@make_request(request)
def get_tournament_matches_ids(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@match.route('/matches/<int:matchId>', methods=['GET'])
@make_request(request)
def get_match_by_id(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@match.route(
    '/matches/<int:matchId>/by-tournament-code/<string:tournamentCode>', 
    methods=['GET'])
@make_request(request)
def get_tournament_match(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@match.route('/matchlists/by-account/<int:accountId>', methods=['GET'])
@make_request(request)
def get_ranked_matchlist_for_account(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@match.route('/matchlists/by-account/<int:accountId>/recent', methods=['GET'])
@make_request(request)
def get_last_20_ranked_games_for_account(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@match.route('/timelines/by-match/<int:matchId>', methods=['GET'])
@make_request(request)
def get_match_timeline(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response