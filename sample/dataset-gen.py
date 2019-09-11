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
SQM_TO_SQFT = 10.7639


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


def prepare_tcad_data(df):
    """Prepare and clean up the TCAD DataFrame."""
    # Remove entries with duplcated GEO_ID.
    df.drop_duplicates(subset=["GEO_ID"], inplace=True)

    # Normalize suffixes.
    df["SITUS_STREET_SUFFIX"] = df.SITUS_STREET_SUFFIX.apply(normalize_suffix)

    # Create the lookup column.
    df["addr"] = (
        df.SITUS_NUM.str.strip() + " " + df.SITUS_STREET.str.strip() + " " + df.SITUS_STREET_SUFFIX.str.strip()
    )
    df["addr"] = df["addr"].str.lower()

    # Remove entries with duplcated addr.
    df.drop_duplicates(subset=["addr"], inplace=True)


def prepare_osm_data(df):
    """Prepare and clean up the OSM DataFrame."""
    # Create the lookup column.
    df["addr"] = df.addr_house.str.strip() + " " + df.addr_stree.str.strip()
    df["addr"] = df["addr"].str.lower()

    # Remove entries with duplcated addr.
    df.drop_duplicates(subset=["addr"], inplace=True)

    # Calculate the building footprint.
    df["footprint"] = df.geometry.map(lambda x: calarea(x.__geo_interface__) * SQM_TO_SQFT)

    # Filter by building types.
    df = df.loc[(df["building"] == "house") | (df["building"] == "apartments")]
    return df


def main():
    """Define the main function."""
    # Load the data sets.
    osm_df = gpd.read_file(OSM_SAMPLE_FILE)
    tcad_df = pd.read_csv(TCAD_SAMPLE_FILE)

    # Data cleanup.
    prepare_tcad_data(tcad_df)
    osm_df = prepare_osm_data(osm_df)

    # Merge on exact matches only.
    joined = pd.merge(tcad_df, osm_df, on="addr")

    # DEBUG.
    print(f"OSM shape: {osm_df.shape}")
    print(f"TCAD shape: {tcad_df.shape}")
    print(f"Joined shape: {joined.shape}")

    # Create a new empty dataframe.
    ndf = pd.DataFrame(
        columns=[
            "geo_id",
            "address",
            "type",
            "units",
            "occupants",
            "acreage",
            "footprint",
            "impervious cover",
            "impervious cover per capita",
        ]
    )

    # Populate it.
    ndf["geo_id"] = joined.GEO_ID
    ndf["address"] = joined.addr
    ndf["type"] = joined.building
    ndf["acreage"] = joined.LAND_ACRES * ACRE_TO_SQFT
    ndf["footprint"] = joined["footprint"]
    ndf["impervious cover"] = ndf["footprint"] / ndf["acreage"]

    # Clean it.
    ndf.dropna(subset=["impervious cover"], inplace=True)

    # Save it.
    ndf.to_csv("output.csv")


if __name__ == "__main__":
    main()
