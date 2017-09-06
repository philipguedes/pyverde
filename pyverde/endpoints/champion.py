from flask import Blueprint, request


__prefix = '/lol/platform/v3/champions'
champion = Blueprint('champion', __name__, url_prefix=__prefix)


@champion.route('/', methods=['GET'])
def get_champion_list():
    x = request.args.get('freeToPlay')
    return "OK MANO: " + str(x)


@champion.route('/<int:cid>', methods=['GET'])
def get_champion_information(cid):
    return 'OK MANO COM ID ' + str(cid)