import requests
from flask import Blueprint, request
from pyverde.decorators import make_request


__prefix = '/lol/league/v3'
league = Blueprint('league', __name__, url_prefix=__prefix)


@league.route('/challengerleagues/by-queue/<string:queue>', methods=['GET'])
@make_request(request)
def get_challenger_league_by_queue(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@league.route('/leagues/by-summoner/<int:summonerId>', methods=['GET'])
@make_request(request)
def get_leagues_by_summoner(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@league.route('/masterleagues/by-queue/<string:queue>', methods=['GET'])
@make_request(request)
def get_master_league_by_queue(**kwargs):
    url = kwargs['url']
    print(url)
    response = requests.get(url)
    return response


@league.route('/positions/by-summoner/<int:summonerId>', methods=['GET'])
@make_request(request)
def get_leagues_position_by_summoner(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response