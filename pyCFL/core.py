
import urllib.request, json, re

class cflAPI(object):

    def __init__(self):
        self.base_url = 'http://api.cfl.ca/v1'
        print('cflAPI initiated')

    def _get_games_data(self):
        api_url = self.base_url
        with urllib.request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
        return(data)

    def _set_api_key(self, api_key):
        self.api_key = api_key

    def _build_url(self, url):
        try:
            if re.search('\?', url):
                url = url + '&key=' + self.api_key
            else:
                url = url + '?key=' + self.api_key
        except:
            print("API must be set first using _set_api_key('YOUR_API_KEY')")
