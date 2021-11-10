import requests
import json


def get_collections() -> json:
    """
    Gets the collections that are available from OpenLandMap.
    :return: Returns a list of the available collections.
    """
    response = requests.get("https://api.openlandmap.org/query/collections")
    return response.json()


def get_layers(collection) -> list[json]:
    """
    Gets the layers that are available for a given 'collection' or list of 'collection's.
    :param: A string or list that will be appended to the end of query url, used to specify the target collection
    :returns: If 'collection' is a string, Returns a list containing a single json file containing the information for the provided layer. \
        If 'collection' is empty or not a string, Returns a list containing a single json that contains all layers. If 'collection' is a list, \
        a list of json objects is returned
    """
    if isinstance(collection, list):
        responses = []
        for item in list:
            response = requests.get('https://api.openlandmap.org/query/layers?coll={}'.format(item))
            responses.append(response.json())
        return responses

    if isinstance(collection, str) and collection:
        response = requests.get('https://api.openlandmap.org/query/layers?coll={}'.format(collection))

    else:
        response = requests.get('https://api.openlandmap.org/query/layers?coll=all')

    return [response.json()]


def get_populate() -> json:
    """
    Gets the layers for front-end to populate the menu.
    :return: Returns a json file containing layer information.
    """
    response = requests.get("https://api.openlandmap.org/query/populate")
    return response.json()
