import requests
from flask import Blueprint, request
from pyverde.decorators import make_request


__prefix = '/lol/champion-mastery/v3'
champion_mastery = Blueprint('champion-mastery', __name__, url_prefix=__prefix)


@champion_mastery.route('/scores/by-summoner/<int:summonerId>', methods=['GET'])
@make_request(request)
def get_total_mastery_score(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@champion_mastery.route('/champion-masteries/by-summoner/<int:summonerId>', methods=['GET'])
@make_request(request)
def get_all_champion_mastery(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@champion_mastery.route(
    '/champion-masteries/by-summoner/<int:summonerId>/by-champion/<int:championId>',
    methods=['GET'])
@make_request(request)
def get_specific_champion_mastery(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response