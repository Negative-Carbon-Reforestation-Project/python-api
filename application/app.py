import pandas as pd
import requests_cache

from models import open_land_map as olm


def main():
    print(olm.get_collections())
    print('------------------------------------------------')
    print(olm.get_layers())
    print('------------------------------------------------')
    print(olm.get_populate())
    print('------------------------------------------------')
    print(olm.get_point((-122.0205, 47.6936)))


if __name__ == "__main__":
    requests_cache.install_cache("open_land_map_cache")
    main()
