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

Getting all sites:
```
sites = se_client.sites.get_sites()
```
