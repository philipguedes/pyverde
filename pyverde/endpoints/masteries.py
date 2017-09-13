import requests
from flask import Blueprint, request
from pyverde.decorators import make_request

__prefix = '/lol/platform/v3/masteries'
masteries = Blueprint('masteries', __name__, url_prefix=__prefix)


@masteries.route('/by-summoner/<int:summonerId>')
@make_request(request)
def get_summoner_mastery_pages(**kwargs):
    url = kwargs['url']
    response = requests.get(url)
    return response