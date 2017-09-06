from flask import Blueprint


__prefix = '/lol/champion-mastery/v3'
champion_mastery = Blueprint('champion-mastery', __name__, url_prefix=__prefix)


@champion_mastery.route('/scores/by-summoner/<int:summonerId>', methods=['GET'])
def get_total_mastery_score(summonerId):
    message = "OK\nsummonerId={}".format(summonerId)
    return message


@champion_mastery.route('/champion-masteries/by-summoner/<int:summonerId>', methods=['GET'])
def get_all_champion_mastery(summonerId):
    message = "OK\nsummonerId={}".format(summonerId)
    return message


@champion_mastery.route(
    '/champion-masteries/by-summoner/<int:summonerId>/by-champion/<int:championId>',
    methods=['GET'])
def get_specific_champion_mastery(summonerId, championId):
    message = "testando auto reload\nOK\nsummonerId={}\nchampionId={}".format(summonerId, championId)
    return message