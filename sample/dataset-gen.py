"""
Generates a data set for impervious cover per capita.

Links:
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html
- https://geopandas.readthedocs.io/en/latest/gallery/create_geopandas_from_pandas.html
- https://github.com/scisco/area
"""
import geopandas as gpd
import pandas as pd
import pyproj
from area import area as calarea
import json

OSM_SAMPLE_FILE = "osm-sample.geojson"
TCAD_SAMPLE_FILE = "tcad-sample.json"
M_TO_FT = 10.7639


def main():
    """Define the main function."""
    # Load the data sets.
    osm_df = gpd.read_file(OSM_SAMPLE_FILE)
    tcad_df = pd.read_json(TCAD_SAMPLE_FILE)
    osm_file = open(OSM_SAMPLE_FILE)
    osm_json = json.load(osm_file)
    
    # Calculate the building area
    area_list = []
    for i in range(len(osm_json['features'])):
        #print(osm_json['features'][i]['geometry'])        
        #print(calarea(osm_json['features'][i]['geometry'])*M_TO_FT)
        area_list.append(calarea(osm_json['features'][i]['geometry'])*M_TO_FT)
    osm_df["building area"] = area_list
    
    # Create the lookup column.
    osm_df["addr"] = (
        osm_df.addr_house.values[0].strip().lower()
        + " "
        + osm_df.addr_stree.values[0].strip().lower()
    )
    
    tcad_df["addr"] = (
        tcad_df.SITUS_NUM.map(str)
        + " "
        + tcad_df.SITUS_STREET.values[0].strip().lower()
        + " "
        + tcad_df.SITUS_STREET_SUFFIX.values[0].strip().lower()
    )
    #print(tcad_df.head())

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
    ndf["ground floor area"] = osm_df["building area"]
    
if __name__ == "__main__":
    main()
