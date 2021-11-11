import pandas as pd
import requests_cache

from models import open_land_map as olm


def main():
    # olm_df = pd.DataFrame(olm.some_api_call())
    # print(olm_df.head())

    layers = olm.get_layers()
    layers2 = olm.get_layers2()


if __name__ == "__main__":
    requests_cache.install_cache("open_land_map_cache")
    main()
