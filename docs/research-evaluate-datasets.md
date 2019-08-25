# Research and evaluate existing data sets

## General considerations

The `geometry` field can be used to:

* Deduct the zipcode from the geometry using the lookup service
[get-directions](https://www.get-direction.com/zip-code-lookup.html).
* Compute the area using the geometry with the [fiona](https://fiona.readthedocs.io/en/latest/) and
[pyshp](https://github.com/GeospatialPython/pyshp) libraries. However it produced a unitless result, for example
`6.374564927874783e-08` which I am not sure how to interpret.

## Evaluations

* Austin Open Data Portal: [Building Footprints Year 2013](evaluate/opd-building-footprints-2013.md)
* OpenStreeMap: [Austin, TX](evaluate/osm-austin-texas.md)
