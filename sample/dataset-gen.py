"""
Generates a data set for impervious cover per capita.

Links:
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html
- https://geopandas.readthedocs.io/en/latest/gallery/create_geopandas_from_pandas.html
- https://github.com/scisco/area
"""
import json

from area import area as calarea
import geopandas as gpd
import pandas as pd


OSM_SAMPLE_FILE = "osm-sample.geojson"
TCAD_SAMPLE_FILE = "tcad-sample.json"


def area(geometry):
    """Compute the area of a polygon."""
    SQM_TO_SQFT = 10.7639
    area_list = []
    g = geometry.to_json()
    polygon = json.loads(g)
    coordinates = polygon["features"][0]["geometry"]
    area_list.append(calarea(coordinates) * SQM_TO_SQFT)
    return area_list


def main():
    """Define the main function."""
    # Load the data sets.
    osm_df = gpd.read_file(OSM_SAMPLE_FILE)
    tcad_df = pd.read_json(TCAD_SAMPLE_FILE)

    # Calculate the building area.
    osm_df["building area"] = area(osm_df.geometry)

    # Create the lookup column.
    osm_df["addr"] = osm_df.addr_house.values[0].strip() + " " + osm_df.addr_stree.values[0].strip()
    osm_df["addr"] = osm_df["addr"].str.lower()
    tcad_df["addr"] = (
        tcad_df.SITUS_NUM.map(str)
        + " "
        + tcad_df.SITUS_STREET.values[0].strip()
        + " "
        + tcad_df.SITUS_STREET_SUFFIX.values[0].strip()
    )
    tcad_df["addr"] = tcad_df["addr"].str.lower()

    # Merge on exact matches only.
    join_column = pd.merge(tcad_df, osm_df, on="addr")

    # Create a new empty dataframe.
    ndf = pd.DataFrame(
        columns=[
            "address",
            "units",
            "occupants",
            "acreage",
            "ground floor area",
            "land/floor ratio",
            "impervious cover per capita",
        ]
    )

    # Populate it.
    ndf["address"] = osm_df.addr
    ndf["acreage"] = (tcad_df.LEGAL_ACREAGE / 10000) * 43560
    ndf["ground floor area"] = osm_df["building area"]
    ndf["land/floor ratio"] = ndf["ground floor area"] / ndf["acreage"]

    # Save it.
    ndf.to_csv("output.csv")


if __name__ == "__main__":
    main()
