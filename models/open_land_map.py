import requests

def get_collections() -> list[str]:
    """
    Gets the collections that are available from OpenLandMap.
    :return: Returns a list of the available collections.
    """
    response = requests.get("https://api.openlandmap.org/query/collections")
    return response.json()

def get_layers(collection):
    """
    Gets the layers that are available for a given 'collection'.
    :param: A string that will be appended to the end of query url, used to specify the target collection
    :returns: Returns a json file containing the information for the provided layer
    :returns: Returns a json containing all layers if 'collection' is empty or not a string
    """
    if isinstance(collection, str) and collection:
        response = requests.get('https://api.openlandmap.org/query/layers?coll={}'.format(collection))

    else:
        response = requests.get('https://api.openlandmap.org/query/layers?coll=all')

    return response.json()
