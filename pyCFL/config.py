import json, os

class Settings(object):
    def __init__(self):
        self.read_settings()
        self.set_exports()

    def get_settings(self):
        return (self._settings)

    def read_settings(self):
        try:
            with open('config.json', 'r') as fh:
                self._settings = json.loads(fh.read())
        except:
            print("The config.json file does not exist")
            print(os.path.curdir)

    def set_exports(self):
        _settings = self.get_settings()
        self.api_key = self._settings['api_key']


if __name__ == "__main__":
    settings = Settings()



