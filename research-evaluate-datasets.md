# Research and evaluate existing data sets

## Building Footprints Year 2013

**Source**: Austin Open Data Portal -- https://data.austintexas.gov/Locations-and-Maps/Building-Footprints-Year-2013/7bns-7teg

### Evaluation

The data set is a collection of `Features` where each feature represents a building.

Useful fields from this data set are:

* `max_height`: describe the height of a building in feet.
* `geometry`: represents the shape of the building. It can be used to compute the area, or deduct the zip code

Other than that, the data set is mediocre:

* All the buildings are of type "Structure".
  * Based on the definition of a High rise: 12 stories / 35m / 155 ft ([Skyscraperpage](https://skyscraperpage.com/site/faq/#2), 
  [Wikipedia](https://en.wikipedia.org/wiki/High-rise_building)) we would be able to the categorize each entry in "High rise" or 
  "Non high rise", but that's pretty much it.
* I had to deduct the zipcode from the geometry using the lookup service
[get-directions](https://www.get-direction.com/zip-code-lookup.html).
* I was able to compute the area using the geometry with the [fiona](https://fiona.readthedocs.io/en/latest/) and
[pyshp](https://github.com/GeospatialPython/pyshp) libraries. However it produced a unitless result, for example
`6.374564927874783e-08` which I am not sure how to interpret.

#### Example of one feature

```json
{
  "features": [
    {
      "type": "Feature",
      "properties": {
        "source": "Imagery 2012",
        "feature": "Structure",
        "max_height": "14.52",
        "objectid": "227553",
        "origin_feature_class": "Building_Footprints_2013",
        "elevation": "466.31",
        "base_elevation": "451.79",
        "building_footprints_2013_id": "227553"
      },
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [
                -97.686747517843,
                30.262329330716
              ],
              [
                -97.686631905288,
                30.262300609881
              ],
              [
                -97.686673257617,
                30.262175175196
              ],
              [
                -97.686820876354,
                30.262211846985
              ],
              [
                -97.686779524201,
                30.262337281718
              ],
              [
                -97.686747517843,
                30.262329330716
              ]
            ]
          ]
        ]
      }
    }
  ]
}
```
