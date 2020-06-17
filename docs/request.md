# `tng.request`

This module provides a class for querying the Illustris TNG API.

## Class `tng.request.TNGRequest`

A wrapper class for the TNG API.

### **Methods:**

### `__init__(self, simulation: str, keyfile: str)`

Constructor. Creates a request object for a given simulation.

**Parameters:**
- **simulation**: the TNG simulation to query
- **keyfile**: path to a JSON file that contains request headers (including 'API_KEY')

### `get(self, endpoint, params=None, logfile=None, filename=None)`

Retrieves data from the passed endpoint.

If the response is binary file, the data is saved as 'filename' or the name in the response, if the former is not provided.
If the response is JSON, it is automatically parsed.

**Parameters:**
- **endpoint**: the API endpoint to query
- **params**: a dict object with any query params
- **logfile**: a file in which to record all requests made

**Returns:** A JSON, a filename, or a response object 

### `list_snapshot(self, snapshot=99, start=0, quantity=100, sort_params=dict(), logfile=None)`

Lists the different subhalos in the snapshot that match the sort_params.

**Parameters:**
- **snapshot**: the snapshot to list
- **start**: the index of the first result to be considered
- **quantity**: the number of subhalos to list
- **sort_params**: how to sort the snapshot
- **logfile**: a file in which to record all requests made

**Returns:** A JSON object (represented as a Python dictionary)

### `get_subhalo_json(self, snapshot, subhalo_id, logfile=None)`

Gets JSON data for requested subhalo.

**Parameters:**
- **subhalo_id**: the subhalo to get
- **snapshot**: the snapshot to search
- **logfile**: a file in which to record all requests made

**Returns:** A JSON object (represented as a Python dictionary)


### `get_subhalo_image(self, snapshot, subhalo, params=dict(), logfile=None)`

Gets the visualization for the galaxy specified by the snapshot and subhalo

See [https://www.tng-project.org/data/vis/](https://www.tng-project.org/data/vis/) for potential visualization specifications. Default specifications:
- partType: 'stars',
- partField: 'stellarComp-jwst_f200w-jwst_f115w-jwst_f070w'
- size: 75
- sizeType: 'kpc' 
- method: 'sphMap'
- nPixels: '1024,1024'
- rasterPx: 1100
- rotation: 'face-on'
- plotStyle: 'open'

**Parameters:**
- **snapshot**: snapshot to consider
- **subhalo_id**: subhalo to get the image for
- **params**: dict of image specifications
- **logfile**: a file in which to record all requests made (optional)

**Returns:** A PIL Image