import requests
from flask import Blueprint, request
from pyverde.decorators import make_request


__prefix = '/lol/summoner/v3/summoners'
summoner = Blueprint('summoner', __name__, url_prefix=__prefix)


@summoner.route('/by-account/<int:accountId>', methods=['GET'])
@make_request(request)
def get_summoner_by_account_id(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@summoner.route('/by-name/<string:summonerName>', methods=['GET'])
@make_request(request)
def get_summoner_by_name(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@summoner.route('/<int:summonerId>', methods=['GET'])
@make_request(request)
def get_summoner_by_id(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response
    