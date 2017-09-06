from flask import Blueprint


__prefix = '/lol/platform/v3/masteries'
masteries = Blueprint('masteries', __name__, url_prefix=__prefix)


@masteries.route('/by-summoner/<int:summonerId>')
def get_summoner_mastery_pages(summonerId):
    return "OK"
