import requests
import json
from PIL import Image
from io import BytesIO

"""
TNGRequest.py

This class creates an API wrapper to a specific simulation within the Illustris
TNG project, making it easier to retrieve information. For help, see __main__
below, or go to: https://github.com/aramuk/img-analysis-spiral/tree/master/illustris

"""

TNG_SIMULATIONS = {"TNG100-1", "TNG100-1-Dark", "TNG100-2", "TNG100-2-Dark", "TNG100-3", "TNG100-3-Dark", "TNG300-1", "TNG300-1", "TNG300-2", "TNG300-2", "TNG300-3"}

class TNGRequest():

    def __init__(self, simulation: str, keyfile: str):
        """Creates a TNGRequest that queries the passed 'simulation' name from Illustris-TNG using the API key in 'keyfile'"""
        if simulation not in TNG_SIMULATIONS:
            raise ValueError(f'{simulation} is not a valid TNG simulation')
        self.simulation = simulation
        self.base_url = f'http://www.tng-project.org/api/{simulation}/'
        self.headers = json.loads(open(keyfile).read()) 
    

    def get(self, endpoint, params=None, logfile=None, filename=None):
        """Makes a GET request to the API using the credentials provided"""
        r = requests.get(self.base_url + endpoint, params=params, headers=self.headers)
        r.raise_for_status()
        if logfile:
            logfile.write(f'[{r.headers["Date"]}] GET {r.url} {r.status_code} {r.headers["Content-Length"]}' + '\n')
        # Handle a JSON response
        if r.headers['content-type'] == 'application/json':
            return r.json()
        # Handle a binary file response
        if 'content-disposition' in r.headers:
            outfile = filename or r.headers['content-disposition'].split("filename=")[1]
            with open(outfile, 'wb') as f:
                f.write(r.content)
            return outfile
        return r


    def list_snapshot(self, snapshot=99, start=0, quantity=100, sort_params=dict(), logfile=None):
        """Gets the requested snapshot data from TNG100-1"""
        endpoint = f'snapshots/{snapshot}/subhalos/'
        sort_params['limit'] = quantity if type(quantity) == int and 1 <= quantity <= 100 else 100
        sort_params['offset'] = start
        return self.get(endpoint, sort_params, logfile=logfile)


    def get_subhalo_json(self, snapshot, subhalo_id, logfile=None):
        """Gets JSON data for requested subhalo"""
        endpoint = f'snapshots/{snapshot}/subhalos/{subhalo_id}'
        return self.get(endpoint, logfile=logfile)


    def get_subhalo_image(self, snapshot, subhalo, params=dict(), logfile=None):
        """Gets the visualization for the galaxy specified by the snapshot and subhalo"""
        DOWNLOAD_PARAMS = {
            'partType': 'stars',
            'partField': 'stellarComp-jwst_f200w-jwst_f115w-jwst_f070w',
            'size': 75,
            'sizeType': 'kpc', 
            'method': 'sphMap',
            'nPixels': '1024,1024',
            'rasterPx': 1100,
            'rotation':'face-on',
            'plotStyle':'open'
        }
        DOWNLOAD_PARAMS.update(params)
        endpoint = f'/snapshots/{snapshot}/subhalos/{subhalo}/vis.png'
        response = self.get(endpoint, DOWNLOAD_PARAMS, logfile)
        return Image.open(BytesIO(response.content))
    
    @staticmethod
    def save_image(image: Image, path: str):
        """Saves the passed image object to the passed path"""
        image = image.crop((120, 44, 1102, 1030))
        image.save(path)
        # image.show()

if __name__ == '__main__':
    # Creating an instance of TNGRequest
    # Put API keys in a seperate file for security reasons
    tng = TNGRequest('TNG100-1', 'api-key.json')

    # Query an endpoint
    #   - endpoint: the API endpoint to query
    #   - params: a dict object with any query params (optional)
    #   - logfile: a file in which to record all requests made (optional)
    # returns .json responses as a dict, other formats as Request.Response
    image = tng.get('snapshots/99/subhalos/468590/vis.png', params={'partType': 'stars'}, logfile=open('log.txt','w'))
    
    # List the subhalos in a snapshot of the simulation
    #   - snapshot: snapshot with the simulation to consider (default=99)
    #   - start: entry to start at (default=0)
    #   - quantity: number of subhalos to list; max 100 (default=100)
    #   - sort_params: ways to sort the snapshot (optional)
    #   - logfile: a file in which to record all requests made (optional)
    # returns a dict of up 100 relevant subhalos
    response = tng.list_snapshot(snapshot=99, start=50, quantity=50, sort_params={'halfmassrad_stars__lte': 10.0}, logfile=open('log.txt','w'))
    subhalos = response['results']

    # Get the .json data for a singular subhalo
    #   - snapshot: snapshot to consider
    #   - subhalo_id: subhalo to get the .json for
    #   - logfile: a file in which to record all requests made (optional)
    # returns a dict with data for the passed subhalo_id
    subhalo_data = tng.get_subhalo_json(99, 468590, logfile=open('log.txt','w'))

    # Visualize a subhalo
    #   - snapshot: snapshot to consider
    #   - subhalo_id: subhalo to get the image for
    #   - params: dict of image specifications
    #   - logfile: a file in which to record all requests made (optional)
    # returns a PIL.Image object of the visualization
    image = tng.get_subhalo_image(99, 468590, params={'partType':'gas'}, logfile=open('log.txt','w')) 
    image.show()
