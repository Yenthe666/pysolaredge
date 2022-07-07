import requests
from ..api.error import IdentifierError
BASE_URL = 'https://monitoringapi.solaredge.com'


class Battery(object):

    """
        Object for getting API details about batteries related to a site
    """
    def __init__(self, client):
        self.client = client

    def get_site_storage_data(self, site_id, startTime, endTime):
        """
            Returns the Storage data(Battery) for a specific site.
            Parameters:
                site_id (int): the ID of a site location (can be fetched from the get_sites function)
                startTime (datetime): the start date and time of the data.
                endTime (datetime): the end date and time of the data.
            Returns:
                response (JSON): a JSON dictionary containing the battery data
        """
        if not site_id:
            raise IdentifierError("This API call needs to have a site_id.")
        if not startTime:
            raise IdentifierError("This API call needs to have startTime.")
        if not endTime:
            raise IdentifierError("This API call needs to have endTime.")

        api_endpoint = '/site/%s/storageData' % site_id
        full_api_url = BASE_URL + api_endpoint
        response = requests.get(full_api_url, params={
            'api_key': self.client.get_api_key(),
            'startTime': startTime.strftime("%Y-%m-%d %H:%M:%S"),
            'endTime': endTime.strftime("%Y-%m-%d %H:%M:%S")
        })
        return response.json()
