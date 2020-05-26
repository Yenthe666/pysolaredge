import requests
from ..api.error import IdentifierError
BASE_URL = 'https://monitoringapi.solaredge.com'


class Equipment(object):
    """
        Object for getting API details about equipments related to a site
    """
    def __init__(self, client):
        self.client = client

    def get_site_equipment(self, site_id):
        """
            Returns the equipments for a specific site.
            Parameters:
                site_id (int): the ID of a site location (can be fetched from the get_sites function)
            Returns:
                response (JSON): a JSON dictionary containing the equipment data
        """
        if not site_id:
            raise IdentifierError("This API call needs to have a site_id.")

        api_endpoint = '/equipment/%s/list' % site_id
        full_api_url = BASE_URL + api_endpoint
        response = requests.get(full_api_url, params={'api_key': self.client.get_api_key()})
        return response.json()
