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
    osm_df = gpd.read_file(OSM_SAMPLE_FILE, driver="GeoJSON")
    tcad_df = pd.read_json(TCAD_SAMPLE_FILE)


if __name__ == "__main__":
    main()
