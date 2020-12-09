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

    def get_inverter_technical_data(self, site_id, serial_number, startTime, endTime):
        """
            Returns the inverters technical data for a specific site.
            Parameters:
                site_id (int): the ID of a site location (can be fetched from the get_sites function).
                serial_number (str): the serial number of the inverter.
                startTime (datetime): the start date and time of the data.
                endTime (datetime): the end date and time of the data.
            Returns:
                response (JSON): a JSON dictionary containing the inverter technical data.
        """
        if not site_id:
            raise IdentifierError("This API call needs to have a site_id.")
        if not serial_number:
            raise IdentifierError("This API call needs to have a serial_number.")

        api_endpoint = '/equipment/%s/%s/data' % (site_id, serial_number)
        full_api_url = BASE_URL + api_endpoint
        parameters = {
            'startTime': startTime.strftime("%Y-%m-%d %H:%M:%S"),
            'endTime': endTime.strftime("%Y-%m-%d %H:%M:%S"),
            'api_key': self.client.get_api_key()
        }
        response = requests.get(full_api_url, params=parameters)
        return response.json()

