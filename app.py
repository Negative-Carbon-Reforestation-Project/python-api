import pandas as pd
import open_land_map as olm


def main():
    olm_df = pd.DataFrame(olm.some_api_call())
    print(olm_df.head())


if __name__ == "__main__":
    main()
