import os
import urllib.parse as parse
from urllib.parse import urlparse, parse_qsl, urlencode


REGION = os.getenv('API_REGION', 'br1')
API_KEY = os.getenv('API_KEY', '')


def get_url(path):
    base_url = "https://{}.api.riotgames.com".format(REGION)
    parsed_url = urlparse(path)
    query = dict(parse_qsl(parsed_url.query))
    query.update({'api_key': API_KEY})
    encoded_query = urlencode(query)
    return "{}{}?{}".format(base_url, parsed_url.path, encoded_query)