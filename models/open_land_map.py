import requests
from typing import List, Dict


def get_collections() -> List[str]:
    """
    Gets the collections that are available from OpenLandMap.
    :return: Returns a list of the available collections.
    """
    response = requests.get("https://api.openlandmap.org/query/collections")
    if response.status_code == 200:  # if query was successful return json of response body
        return response.json()
    else:  # if query was not successful return ConnectionRefusedError
        raise ConnectionRefusedError(f'There was an error when querying a collection, please check your '
                                     f'internet connection. Status code: {response.status_code}')


def get_layers(collection: str = "all") -> Dict[str, List[Dict[str, str]]]:
    response = requests.get(f"https://api.openlandmap.org/query/layers?coll={collection}")
    if response.status_code == 200:  # if query was successful return json of response body
        return response.json()
    else:  # if query was not successful return ConnectionRefusedError
        raise ConnectionRefusedError(f'There was an error when getting a layer, please ensure collection is a string '
                                     f'expected by the API and that you are connected to the internet. '
                                     f'Status code: {response.status_code}')


def get_populate() -> Dict[str, List[Dict[str, str]]]:
    """
    Gets the layers for front-end to populate the menu.
    :return: Returns a json file containing layer information.
    """
    response = requests.get("https://api.openlandmap.org/query/populate")
    if response.status_code == 200:  # if query was successful return json of response body
        return response.json()
    else:  # if query was not successful return ConnectionRefusedError
        raise ConnectionRefusedError(f'There was an error when getting populate, '
                                     f'make sure you are connected to the internet '
                                     f'Status code: {response.status_code}')


def get_point(point: tuple,
              coll: str = 'layers250m',
              code: str = '(.*)',
              variable: str = '(.*)',
              procedure: str = '(.*)',
              probability: str = '(.*)',
              resolution: str = '(.*)',
              depth: str = '(.*)',
              time: str = '(.*)',
              version: str = '(.*)',
              regex: str = '',
              root_dir: str = '/data/layers_to_display/') -> requests.models.Response:
    """
    gets all layers at a point given filters
    :param point: a point of format (latitude, longitude) required
    :param coll: a collection of layers. default='layers250m'
    :param code: theme code. default='(.*)'
    :param variable: generic variable name. default='(.*)'
    :param procedure: variable procedure combination (standard abbreviation). default='(.*)'
    :param probability: position in the probability distribution / variable type. default='(.*)'
    :param resolution: resolution. default='(.*)'
    :param depth: depth reference or depth interval
                  e.g. “b0..10cm” below ("b"), above ("a") ground or ("s") default='(.*)'
    :param time: time reference default='(.*)'
    :param version: version of the map (major release - update - bug fix) default='(.*)'
    :param regex: regular expression or string default=''
    :param root_dir: directory default='/data/layers_to_display/'
    :return: json response of filtered layers available at a given point
    """
    if not isinstance(point, tuple):  # if point is not a tuple raise new type error
        raise TypeError('point must be of type tuple (latitude, longitude)')
    if not len(point) == 2:  # if point is not of length two raise new value error
        raise ValueError('point must be of format (latitude, longitude)')
    if not isinstance(point[0], float) and isinstance(point[1], float):  # if point is not a float raise new value error
        raise ValueError('point values must be of type float (latitude: float, longitude: float)')
    if point[0] < -180 or point[1] > 180:  # if latitude is out of bounds raise new value error
        raise ValueError('latitude must be between [-180.0000, 180.0000] degrees')
    if point[1] < -90 or point[0] > 90:  # if longitude is out of bounds raise new value error
        raise ValueError('longitude must be between [-90.0000, 90.0000] degrees')

    if len(regex) > 0:  # if regex is used include it
        response = requests.get(f'https://api.openlandmap.org/query/point?'
                                f'lon=lon{point[1]}&'
                                f'lat=lat{point[0]}&'
                                f'coll={coll}&'
                                f'code={code}&'
                                f'variable={variable}&'
                                f'procedure={procedure}&'
                                f'probability={probability}&'
                                f'resolution={resolution}&'
                                f'depth={depth}&'
                                f'time={time}&'
                                f'version={version}&'
                                f'regex={regex}&'
                                f'root_dir={root_dir}')
    else:  # otherwise omit regex from the query
        response = requests.get(f'https://api.openlandmap.org/query/point?'
                                f'lon=lon{point[1]}&'
                                f'lat=lat{point[0]}&'
                                f'coll={coll}&'
                                f'code={code}&'
                                f'variable={variable}&'
                                f'procedure={procedure}&'
                                f'probability={probability}&'
                                f'resolution={resolution}&'
                                f'depth={depth}&'
                                f'time={time}&'
                                f'version={version}&'
                                f'root_dir={root_dir}')

    if response.status_code == 200:  # if query was successful return json of response body
        return response.json()
    else:  # if query was not successful return ConnectionRefusedError
        raise ConnectionRefusedError(f'There was an error when querying a point, please ensure all arguments other '
                                     f'than point is a string expected by the API. '
                                     f'Status code: {response.status_code}')
