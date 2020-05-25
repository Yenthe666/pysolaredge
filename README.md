# pysolaredge
Python API wrapper for SolarEdge monitoring


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
