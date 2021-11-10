import requests


def get_layers(collection):
    """
    Gets the layers that are available for a given 'collection'.
    Returns a json file containing the information for the provided layer
    Returns a json containing all layers if 'collection' is empty or not a string
    """
    if isinstance(collection, str) and collection:
        response = requests.get('https://api.openlandmap.org/query/layers?coll={}'.format(collection))

    else:
        response = requests.get('https://api.openlandmap.org/query/layers?coll=all')

    return response.json()
