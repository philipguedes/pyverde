import requests
import pyverde.utils as utils
from flask import Response
from functools import wraps


HEADERS = {"X-App-Rate-Limit",
            "X-App-Rate-Limit-Count",
            "X-Method-Rate-Limit",
            "X-Method-Rate-Limit-Count",
            "Content-Type",
            "Date"}


def make_request(request):
    def wrapper(func):    
        @wraps(func)
        def func_wrapper(**kwargs):
            path = request.environ['REQUEST_URI']
            dst = utils.get_url(path)
            x = func(url=dst, **kwargs)
            headers = {}
            for header, value in x.headers.items():
                if header in HEADERS:
                    headers[header] = value
            response = Response(x, status=x.status_code, headers=headers)
            return response
        return func_wrapper
    return wrapper