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

    def get_inverter_technical_data(self, site_id, serial_number, start_time, end_time):
        """
            Return specific inverter data for a given timeframe.
            Parameters:
                site_id (int): the ID of a site location (can be fetched from the get_sites function)
                serial_number (string): The inverter short serial number
                start_time (string): the start datetime from when you want metrics (in the format yyyy-MM-DD hh:mm:ss)
                end_time (string): the end datetime until when you want metrics (in the format yyyy-MM-DD hh:mm:ss)
            Returns:
                response (JSON): a JSON dictionary containing the response includes technical parameters as for the inverter’s performance (e.g., voltage, current, active
                    power etc.), inverter type (1ph or 3ph), and software version. If an attribute is not supported based on the inverter version
                    or type it will be omitted from the response.
        """
        if not site_id or not serial_number or not start_time or not end_time:
            raise IdentifierError("This API call needs to have a site_id, serial_number, start_time and end_time.")

        api_endpoint = '/equipment/%s/%s/data' % (site_id, serial_number)
        full_api_url = BASE_URL + api_endpoint

        parameters = {
            'startTime': start_time,
            'endTime': end_time,
            'api_key': self.client.get_api_key()
        }

        response = requests.get(full_api_url, params=parameters)
        return response.json()

    def get_equipment_change_log(self, site_id, serial_number):
        """
            Returns a list of equipment component replacements ordered by date. This method is applicable to inverters, optimizers, batteries and gateways.
            Parameters:
                site_id (int): the ID of a site location (can be fetched from the get_sites function)
                serial_number (string): The inverter short serial number
                start_time (string): the start datetime from when you want metrics (in the format yyyy-MM-DD hh:mm:ss)
                end_time (string): the end datetime until when you want metrics (in the format yyyy-MM-DD hh:mm:ss)
            Returns:
                response (JSON): a JSON dictionary containing the response includes a list of replacements by the specified equipment component, 
                    ordered-by date. The list contains the component serial number, model and date of replacement.
        """
        if not site_id or not serial_number:
            raise IdentifierError("This API call needs to have a site_id and serial_number.")

        api_endpoint = '/equipment/%s/%s/changeLog' % (site_id, serial_number)
        full_api_url = BASE_URL + api_endpoint

        parameters = {
            'api_key': self.client.get_api_key()
        }

        response = requests.get(full_api_url, params=parameters)
        return response.json()