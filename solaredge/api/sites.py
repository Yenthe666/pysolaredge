import requests
from ..api.error import IdentifierError
BASE_URL = 'https://monitoringapi.solaredge.com'


class Sites(object):
    """
        Object for getting API details about sites
    """
    def __init__(self, client):
        self.client = client

    def get_total_sites(self, searchText="", status=""):
        """
            Function for getting the amount of sites that are available for a specific search criteria.

            Parameters:
                searchText (string): Search for text in this specific site. It searches through the following options:
                    Name, Notes, Address, City, Zip code, Full address, Country
                 sortProperty (string): on which criteria you would like to sort the sites. It searches through the
                 following options:
                    Name, Country, State, City, Address, Zip, Status, PeakPower, InstallationDate, Amount, MaxSeverity,
                    CreationTime
                status (string): on which site status you would like to filter. Possible options are:
                    Active, Pending, Disabled, All

            Returns:
                total_sites (int): Number of sites matching with this criteria
        """
        api_endpoint = '/sites/list'
        full_api_url = BASE_URL + api_endpoint
        parameters = {
            'status': status,
            'api_key': self.client.get_api_key()
        }

        if searchText:
            parameters['searchText'] = searchText

        total_sites = int(requests.get(full_api_url, params=parameters).json().get('sites').get('count'))
        return total_sites

    def get_sites(self, size=100, startIndex=0, searchText="", sortProperty="", sortOrder="", status=""):
        """
            Function to get all sites attached to an API key (max 100 items at a time)

            Parameters:
                size (int): the amount of sites you'd like to retrieve (which is limited to 100)
                startIndex (int): from which counter you'd like to get back sites. Combined with size this
                    gives back a start and endpoint (for example: startIndex=100, size=50 gives 100-150)
                searchText (string): Search for text in this specific site. It searches through the following options:
                    Name, Notes, Address, City, Zip code, Full address, Country
                 sortProperty (string): on which criteria you would like to sort the sites. It searches through the
                 following options:
                    Name, Country, State, City, Address, Zip, Status, PeakPower, InstallationDate, Amount, MaxSeverity,
                    CreationTime
                sortOrder (string): sort order for the sort property. This can be ASC or DESC.
                status (string): on which site status you would like to filter. Possible options are:
                    Active, Pending, Disabled, All

            Returns:
                response (json): a JSON dictionary with all details about the sites.
                See https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf for more details.
        """
        api_endpoint = '/sites/list'
        full_api_url = BASE_URL + api_endpoint

        if sortOrder:
            # It has to be CAPS for the search criteria.
            sortOrder = str.upper((sortOrder))
            if sortOrder != "ASC" and sortOrder != "DESC":
                raise IdentifierError("sortOrder only accepts 'ASC' or 'DESC' as values.")

        parameters = {
            'size': size,
            'startIndex': startIndex,
            'sortOrder': sortOrder,
            'status': status,
            'api_key': self.client.get_api_key()
        }

        if searchText:
            parameters['searchText'] = searchText

        if sortProperty:
            parameters['sortProperty'] = sortProperty

        response = requests.get(full_api_url, params=parameters)
        return response.json()

    def get_site_details(self, site_id):
        """
            Function to get the details back from a specific site
            Parameters:
                site_id (int): the ID of a site location (can be fetched from the get_sites function)
            Returns:
                response (JSON): a JSON dictionary containing all details about a site location.
        """

        api_endpoint = '/site/%s/details' % site_id
        full_api_url = BASE_URL + api_endpoint
        response = requests.get(full_api_url, params={'api_key': self.client.get_api_key()})
        return response.json()

    def get_multiple_site_details(self, site_ids):
        """
            Function to get the details back from multiple sites
            Parameters:
                site_ids (list): list of IDS for all the site locations you'd like to get details from.
                    For example: [1, 2, 3, 4]
            Returns:
                response (JSON): a JSON dictionary containing the details for multiple sites
        """
        api_endpoint = '/sites/%s/overview' % ','.join(map(str, site_ids))
        full_api_url = BASE_URL + api_endpoint
        response = requests.get(full_api_url, params={'api_key': self.client.get_api_key()})
        return response.json()

    def get_site_start_and_end_dates(self, site_id):
        """
            Returns the start date and the end date of the site location (when it started generating energy)
            Parameters:
                site_id (int): the ID of a site location (can be fetched from the get_sites function)
            Returns:
                response (JSON): a JSON dictionary containing the start date and end date
        """
        if not site_id:
            raise IdentifierError("This API call needs to have a site_id.")
        api_endpoint = '/site/%s/dataPeriod' % site_id
        full_api_url = BASE_URL + api_endpoint
        response = requests.get(full_api_url, params={'api_key': self.client.get_api_key()})
        return response.json()

    def get_energy_details(self, site_id, startDate, endDate, timeUnit):
        """
            Returns the energy detail for a specific site and date range.
            Call get_multiple_energy_details if you'd like to get energy details for multiple locations at once!
            Parameters:
                site_id (int): the ID of a site location (can be fetched from the get_sites function)
                startDate (string): the start date from when you want metrics (in the format YYYY-MM-DD)
                endDate (string): the end date untill when you want metrics (in the format YYYY-MM-DD)
            Returns:
                response (json): a JSON dictionary containing the energy details for a site
        """
        if not site_id or not startDate or not endDate:
            raise IdentifierError("This API call needs to have a site_id, startDate and endDate.")

        api_endpoint = '/site/%s/energy' % site_id
        full_api_url = BASE_URL + api_endpoint

        parameters = {
            'startDate': startDate,
            'endDate': endDate,
            'timeUnit': timeUnit,
            'api_key': self.client.get_api_key()
        }

        response = requests.get(full_api_url, params=parameters)
        return response.json()

    def get_multiple_energy_details(self, site_ids, startDate, endDate, timeUnit):
        """
            Returns the energy detail for multiple sites within a date range.
            Parameters:
                site_ids (list): the IDs of multiple site locations (can be fetched from the get_sites function)
                    For example: [1,2,3,4]
                startDate (string): the start date from when you want metrics (in the format YYYY-MM-DD)
                endDate (string): the end date untill when you want metrics (in the format YYYY-MM-DD)
            Returns:
                response (json): a JSON dictionary containing the energy details for multiple sites
        """
        if not site_ids or not startDate or not endDate:
            raise IdentifierError("This API call needs to have site_ids, a startDate and an endDate.")

        api_endpoint = '/sites/%s/energy' % ','.join(map(str, site_ids))
        full_api_url = BASE_URL + api_endpoint

        parameters = {
            'startDate': startDate,
            'endDate': endDate,
            'timeUnit': timeUnit,
            'api_key': self.client.get_api_key()
        }

        response = requests.get(full_api_url, params=parameters)
        return response.json()
