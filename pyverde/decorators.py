import requests
import pyverde.utils as utils


def make_request(request):
    def wrapper(func):    
        def func_wrapper(**kwargs):
            # print(request.__dict__)
            # print(kwargs)
            # print('do something before')
            path = request.environ['REQUEST_URI']
            url = utils.get_url(path)
            # print(url)
            res = requests.get(url)
            x = func(response=res, **kwargs)
            # print('do something after')
            # print(res)
            return x
        return func_wrapper
    return wrapper