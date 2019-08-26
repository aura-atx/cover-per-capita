# Research and evaluate existing data sets

## General considerations

The `geometry` field can be used to:

* Deduct the zipcode from the geometry using the lookup service
[get-directions](https://www.get-direction.com/zip-code-lookup.html).
* Compute the area using the geometry with the [fiona](https://fiona.readthedocs.io/en/latest/) and
[pyshp](https://github.com/GeospatialPython/pyshp) libraries. However it produced a unitless result, for example
`6.374564927874783e-08` which I am not sure how to interpret.

In order to compare the results to a known building, **when applicable**, all the examples will feature the Sabina property, 3400 Harmon Avenue, Austin TX, 78705.

Relevant facts for our effort:

|Item|Value 1|Value 2|
|---|---|---|
|# of units| 298 |
|Land area| 2.565 acres | 111731.5 sqft |
|Ground floor area| 0.354 acres | 15443 sqft |

Sources:

* [OpenStreetMap](https://www.openstreetmap.org/relation/7480556)
* [Redfin](https://www.redfin.com/TX/Austin/3400-Harmon-Ave-78705/home/52405011)
* [Walkscore](https://www.walkscore.com/score/3400-harmon-ave-austin-tx-78705)
* [Zillow](https://www.zillow.com/b/sabina-austin-tx-5ZcVvx/)

## Evaluations

* Austin Open Data Portal: [Building Footprints Year 2013](evaluate/opd-building-footprints-2013.md)
* OpenStreeMap: [Austin, TX](evaluate/osm-austin-texas.md)
* TCAD: [Austin, TX](evaluate/travis-county-appraisal-database.md)

## Final data set

This is what the final data set should look like and where the data comes from:

|Column|Source|
|---|---|
|Building info|TCAD - *aggregated data*|
|# of units(*)||
|# of occupants||
|Land area (sqft)|TCAD|
|Ground floor area (sqft)|OSM - *computed from geometry*|
|Ground floor/Land Ratio| *computed* |
|Ground floor/# of occupants| *computed* |

(*) The # of units is not necessary per say, but would help in case we cannot get the number of occupants per building.
