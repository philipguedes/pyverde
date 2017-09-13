import requests
from flask import Blueprint, request
from pyverde.decorators import make_request


__prefix = '/lol/platform/v3/runes'
runes = Blueprint('runes', __name__, url_prefix=__prefix)


@runes.route('/by-summoner/<int:summonerId>', methods=['GET'])
@make_request(request)
def get_summoner_rune_pages(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response