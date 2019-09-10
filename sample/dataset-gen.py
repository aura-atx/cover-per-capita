"""
Generates a data set for impervious cover per capita.

Links:
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html
- https://geopandas.readthedocs.io/en/latest/gallery/create_geopandas_from_pandas.html
- https://github.com/scisco/area

Keyword definitions:
- building cover (or "building coverage"): the land or amount of land covered by a building and its roof.
- footprint: the ground covered by a structure.
- impervious cover: land which cannot absorb rainwater, because something waterproof is on top of it.
    E.g., streets, houses, etc. For example, a macadam driveway is impervious cover, but a gravel driveway is not,
    because rainwater can pass through it and be absorbed by the earth underneath it. Impervious cover usually results
    in less greenery, more gutters/sewers, and possibly more flash floods.
"""
import json

from area import area as calarea
import geopandas as gpd
import pandas as pd


OSM_SAMPLE_FILE = "input_datasets/osm-austin/austin-tx_planet_osm_polygon_polygons.shp"
TCAD_SAMPLE_FILE = "input_datasets/tcad/tcad.csv"
ACRE_TO_SQFT = 43560


def compute_area(geometry):
    """Compute the area of a polygon."""
    SQM_TO_SQFT = 10.7639
    g = geometry.to_json()
    polygon = json.loads(g)
    coordinates = polygon["features"][0]["geometry"]
    return calarea(coordinates) * SQM_TO_SQFT


def normalize_suffix(suffix):
    suffixes = {
        "(pvt)": "",
        "ave": "avenue",
        "bend": "",
        "blf": "",
        "blvd": "boulevard",
        "bnd": "",
        "ci": "",
        "cir": "",
        "clf": "",
        "cove": "",
        "crk": "",
        "crt": "",
        "ct": "",
        "cv": "",
        "cyn": "",
        "dr": "",
        "drive": "",
        "dv": "",
        "flds": "",
        "hl": "",
        "holw": "",
        "hwy": "",
        "hy": "",
        "ln": "",
        "lndg": "",
        "loop": "",
        "lp": "",
        "mdws": "",
        "n": "",
        "park": "",
        "parkway": "",
        "pass": "",
        "path": "",
        "pkwy": "",
        "pl": "",
        "place": "",
        "plc": "",
        "ps": "",
        "pt": "",
        "pvt": "",
        "rd": "road",
        "rdg": "",
        "rg": "",
        "row": "",
        "run": "",
        "skwy": "",
        "sq": "",
        "st": "street",
        "ter": "",
        "terr": "",
        "tr": "",
        "trc": "",
        "trce": "",
        "trl": "",
        "view": "",
        "vista": "",
        "vly": "",
        "vw": "",
        "walk": "",
        "way": "",
        "wy": "",
        "xing": "",
    }
    try:
        s = suffixes.get(suffix.lower())
    except:
        s = None
    return s if s else suffix


def main():
    """Define the main function."""
    # Load the data sets.
    osm_df = gpd.read_file(OSM_SAMPLE_FILE)
    tcad_df = pd.read_csv(TCAD_SAMPLE_FILE)
    # , dtype={"PROP_ID": int, "GEO_ID": int}

    # Calculate the building area.
    # Note(rgreinho): I could not find how to extract the right information from a Shapely Polygon, therefore I could
    #   not the apply() function to the whole DataSeries.
    # osm_df["building area"] = osm_df.geometry.apply(compute_area)
    osm_df["footprint"] = compute_area(osm_df.geometry)

    # Normalize suffixes.
    # tcad_df["SITUS_STREET_SUFFIX"] = normalize_suffix(tcad_df.SITUS_STREET_SUFFIX)
    tcad_df["SITUS_STREET_SUFFIX"] = tcad_df.SITUS_STREET_SUFFIX.apply(normalize_suffix)

    # Create the lookup column.
    osm_df["addr"] = osm_df.addr_house.str.strip() + " " + osm_df.addr_stree.str.strip()
    osm_df["addr"] = osm_df["addr"].str.lower()
    tcad_df["addr"] = (
        tcad_df.SITUS_NUM.map(str)
        + " "
        + tcad_df.SITUS_STREET.str.strip()
        + " "
        + tcad_df.SITUS_STREET_SUFFIX.str.strip()
    )
    tcad_df["addr"] = tcad_df["addr"].str.lower()

    # Merge on exact matches only.
    joined = pd.merge(tcad_df, osm_df, on="addr")
    # breakpoint()

    # Create a new empty dataframe.
    ndf = pd.DataFrame(
        columns=[
            "geo_id",
            "address",
            "units",
            "occupants",
            "acreage",
            "footprint",
            "building cover",
            "impervious cover per capita",
        ]
    )

    # Populate it.
    ndf["geo_id"] = joined.GEO_ID
    ndf["address"] = joined.addr
    ndf["acreage"] = joined.LAND_ACRES * ACRE_TO_SQFT
    ndf["footprint"] = joined["footprint"]
    ndf["building cover"] = ndf["footprint"] / ndf["acreage"]

    # Save it.
    ndf.to_csv("output.csv")


if __name__ == "__main__":
    main()
