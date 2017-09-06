from flask import Blueprint, request


__prefix = '/lol/platform/v3/runes'
runes = Blueprint('runes', __name__, url_prefix=__prefix)


@runes.route('/by-summoner/<int:summonerId>', methods=['GET'])
def get_summoner_rune_pages(summonerId):
    return "OK"