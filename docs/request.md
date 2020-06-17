# `tng.request`

This module provides a class for querying the Illustris TNG API.

## `TNGRequest`

A wrapper class for the TNG API.

### Methods

`get(self, endpoint, params=None, logfile=None, filename=None)`
Retrieves data from the passed endpoint.

If the response is binary file, the data is saved as 'filename' or the name in the response, if the former is not provided.
If the response is JSON, it is automatically parsed.

**Parameters:**
- **endpoint**: the API endpoint to query
- **params**: a dict object with any query params
- **logfile**: a file in which to record all requests made

**Returns:** A response object


`list_snapshot(self, snapshot=99, start=0, quantity=100, sort_params=dict(), logfile=None)`
Gets the metrics for the requested snapshot from the simulation.

**Parameters:**
- **snapshot**: the snapshot to list
- **start**: the index of the first result to be considered
- **quantity**: the number of subhalos to list
- **sort_params**: how to sort the snapshot
- **logfile**: a file in which to record all requests made

`get_subhalo_json(self, snapshot, subhalo_id, logfile=None)`
- **subhalo_id**: the subhalo to get
- **snapshot**: the snapshot to search
- **logfile**: a file in which to record all requests made

`get_subhalo_image(self, snapshot, subhalo, params=dict(), logfile=None)`
- **snapshot**: snapshot to consider
- **subhalo_id**: subhalo to get the image for
- **params**: dict of image specifications
- **logfile**: a file in which to record all requests made (optional)
