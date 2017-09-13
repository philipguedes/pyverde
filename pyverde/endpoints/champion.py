import requests
from flask import Blueprint, request
from pyverde.decorators import make_request


__prefix = '/lol/platform/v3/champions'
champion = Blueprint('champion', __name__, url_prefix=__prefix)


@champion.route('/', methods=['GET'])
@make_request(request)
def get_champion_list(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response


@champion.route('/<int:cid>', methods=['GET'])
@make_request(request)
def get_champion_information(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response