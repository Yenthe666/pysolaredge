from .sites import Sites
from .equipment import Equipment
from .battery import Battery


class Client(object):
    def __init__(self):
        self.api_key = None
        self.sites = Sites(self)
        self.equipment = Equipment(self)
        self.battery = Battery(self)

    def set_api_key(self, api_key):
        self.api_key = api_key

    def get_api_key(self):
        return self.api_key
