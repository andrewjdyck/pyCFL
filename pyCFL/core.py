
import urllib.request, json, re
import pyCFL.config as cfg

class cflAPI(object):
    def __init__(self):
        self.base_url = 'http://api.cfl.ca/v1'
        self._set_api_key()

    def _get_games_data(self):
        api_url = self.base_url
        with urllib.request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
        return(data)

    def _set_api_key(self):
        self.api_key = cfg.Settings().api_key
        print('api key is: {}'.format(self.api_key))

    def _build_url(self, url):
        try:
            if re.search('\?', url):
                url = url + '&key=' + self.api_key
            else:
                url = url + '?key=' + self.api_key
        except:
            print("API must be set first using _set_api_key('YOUR_API_KEY')")
