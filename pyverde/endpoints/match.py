from flask import Blueprint, request


__prefix = '/lol/match/v3'
match = Blueprint('match', __name__, url_prefix=__prefix)


@match.route('/matches/by-tournament-code/<string:tournamentCode>/ids', methods=['GET'])
def get_tournament_matches_ids(tournamentCode):
    return "OK"


@match.route('/matches/<int:matchId>', methods=['GET'])
def get_match_by_id(matchId):
    x = request.args.get('forAccountId')

    return 'OK for account id'


@match.route(
    '/matches/<int:matchId>/by-tournament-code/<string:tournamentCode>', 
    methods=['GET'])
def get_tournament_match(matchId, tournamentCode):
    return "OK"


@match.route('/matchlists/by-account/<int:accountId>', methods=['GET'])
def get_ranked_matchlist_for_account(accountId):
    # TODO: Check apidocs for optional query parameters
    return "OK"


@match.route('/matchlists/by-account/<int:accountId>/recent', methods=['GET'])
def get_last_20_ranked_games_for_account(accountId):
    return "OK"


@match.route('/timelines/by-match/<int:matchId>', methods=['GET'])
def get_match_timeline(matchId):
    return "OK"
