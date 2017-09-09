import os

# 813140
# https://br1.api.riotgames.com/lol/summoner/v3/summoners/by-name/czekanie%20masz?api_key=RGAPI-a196b74e-586d-4154-bdd9-f3881e4baa18


REGION = os.getenv('API_REGION', 'br1')
API_KEY = os.getenv('API_KEY', 'RGAPI-a196b74e-586d-4154-bdd9-f3881e4baa18')


def get_url(path):
    url = "https://{}.api.riotgames.com{}?api_key={}".format(REGION, path, API_KEY)
    return url