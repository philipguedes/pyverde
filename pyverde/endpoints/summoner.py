from flask import Blueprint, request


__prefix = '/lol/summoner/v3/summoners'
summoner = Blueprint('summoner', __name__, url_prefix=__prefix)


@summoner.route('/by-account/<int:accountId>', methods=['GET'])
def get_summoner_by_account_id(accountId):
    return "OK"


@summoner.route('/by-name/<string:summonerName>', methods=['GET'])
def get_summoner_by_name(summonerName):
    return "OK"


@summoner.route('/<int:summonerId>', methods=['GET'])
def get_summoner_by_id(summonerId):
    return "OK"