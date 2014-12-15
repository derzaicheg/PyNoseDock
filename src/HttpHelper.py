import requests

class HttpHelper(object):
    def __init__(self):
        pass
     
    def get(self, url, params, headers):
        result = requests.get(url, params=params, headers=headers)
        return result
     
    
# if __name__ == '__main__':
#     h = HttpHelper()
#     h.get('http://httpbin.org', None, None)