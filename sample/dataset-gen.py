"""
Generates a data set for impervious cover per capita.

Links:
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html
- https://geopandas.readthedocs.io/en/latest/gallery/create_geopandas_from_pandas.html
"""
import geopandas as gpd
import pandas as pd

OSM_SAMPLE_FILE = "osm-sample.geojson"
TCAD_SAMPLE_FILE = "tcad-sample.json"


def main():
    """Define the main function."""
    # Load the data sets.
    osm_df = gpd.read_file(OSM_SAMPLE_FILE, driver="GeoJSON")
    tcad_df = pd.read_json(TCAD_SAMPLE_FILE)

    # Create the lookup column.
    osm_df["addr"] = (
        osm_df.addr_house.values[0].strip().lower()
        + " "
        + osm_df.addr_stree.values[0].strip().lower()
    )
    print(osm_df.head())
    tcad_df["addr"] = (
        tcad_df.SITUS_NUM.map(str)
        + " "
        + tcad_df.SITUS_STREET.values[0].strip().lower()
        + " "
        + tcad_df.SITUS_STREET_SUFFIX.values[0].strip().lower()
    )
    print(tcad_df.head())

    # Ensure exact match.
    join_column = tcad_df.where(tcad_df.addr == osm_df.addr)
    assert len(join_column) == 1

    # Create a new empty dataframe.
    ndf = pd.DataFrame(
        columns=[
            "info",
            "units",
            "occupants",
            "land area",
            "ground floor area",
            "land floor ratio",
            "impervious cover per capita",
        ]
    )

    # Populate it.
    ndf["info"] = osm_df.addr
    ndf["land area"] = tcad_df.LEGAL_ACREAGE / 1000


if __name__ == "__main__":
    main()
