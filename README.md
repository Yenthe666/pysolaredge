# pysolaredge
Python API wrapper for SolarEdge monitoring.<br/>
This library allows you to easily communicate with the SolarEdge API to get data about solar installations.<br/>
For more information about the documentation see https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf

# Installation
```
pip3 install py-solaredge
```

# Getting started
Importing the SolarEdge client:
```
from solaredge.api.client import Client
```

Initializing the SolarEdge API client, and setting your API key:
```
se_client = Client()
se_client.set_api_key('XXX')
```
# API's
All of the API classes are available through the client object. `Client()` is the base instance that allows access to the underlying classes and to call API endpoints to get data.
Classes available at this point are `sites` and `equipment`.

## Sites
Getting all sites:
```
sites = se_client.sites.get_sites()
```

Getting the number of sites:
```
number_of_sites = se_client.sites.get_total_sites()
```

## Equipment
Getting the equipment / component list for a location:
```
equipment = se_client.equipment.get_site_equipment('location_id')
```
