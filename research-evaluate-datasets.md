# Research and evaluate existing data sets

## General considerations

The `geometry` field can be used to:

* Deduct the zipcode from the geometry using the lookup service
[get-directions](https://www.get-direction.com/zip-code-lookup.html).
* Compute the area using the geometry with the [fiona](https://fiona.readthedocs.io/en/latest/) and
[pyshp](https://github.com/GeospatialPython/pyshp) libraries. However it produced a unitless result, for example
`6.374564927874783e-08` which I am not sure how to interpret.

## Building Footprints Year 2013

**Source**: Austin Open Data Portal --
https://data.austintexas.gov/Locations-and-Maps/Building-Footprints-Year-2013/7bns-7teg

### Evaluation

The GeoJSON data set was used for this evaluation.

#### Relevant data

| Property | Description |
|---|---|
|entry count| 585916|
|max_height|height of a building in feet|
|geometry| shape of a building|

#### Other findings

Other than that, the data set is not very useful:

* All the buildings are of type "Structure".
  * Based on the definition of a High rise: 12 stories / 35m / 155 ft
  ([Skyscraperpage](https://skyscraperpage.com/site/faq/#2),
  [Wikipedia](https://en.wikipedia.org/wiki/High-rise_building)), we could be able to the categorize each entry in
  "High rise" or "Non high rise", but that's pretty much it.

#### Feature example

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

## Open Street Map

### Evaluation

**Source**: Shapefiles for the city of Austin, TX were generated why the [HOT Export](https://export.hotosm.org/en/v3/) online service, then converted to GeoJSON using [Fiona](https://pypi.org/project/Fiona/).

#### Relevant data

| Property | Description |
|---|---|
|entry count| 447820|
|building| building type ([OSM Key:building](https://wiki.openstreetmap.org/wiki/Key:building))|
|geometry| shape of a building (Note that OSM allows multipolygon structures)|

#### Other findings

The `building` property has 89 possible values, but we could limit our search to only a few types like `house` and
`appartments`. This provides us with 703 entries for appartments, and 4945 entries for houses.

```bash
$ jq '[ .features[] | select(.properties.building == "house")] |length' austin-tx_planet_osm_polygon_polygons.json
703
$ jq '[ .features[] | select(.properties.building == "apartments")] |length' austin-tx_planet_osm_polygon_polygons.json
4945
```

I am not sure how to programatically regenerate the data set.

#### Feature example

```json
{
  "features": [
    {
      "geometry": {
        "coordinates": [
          [
            [
              -97.7382777,
              30.2872101
            ],
            [
              -97.7372907,
              30.2871314
            ],
            [
              -97.7373175,
              30.2868581
            ],
            [
              -97.7373926,
              30.2862559
            ],
            [
              -97.7374468,
              30.2857302
            ],
            [
              -97.7376948,
              30.2857512
            ],
            [
              -97.7376608,
              30.286015
            ],
            [
              -97.7378271,
              30.2860335
            ],
            [
              -97.7378834,
              30.2860995
            ],
            [
              -97.7378969,
              30.2861679
            ],
            [
              -97.7378593,
              30.2862175
            ],
            [
              -97.7378164,
              30.2862744
            ],
            [
              -97.7376394,
              30.2862559
            ],
            [
              -97.7376389,
              30.2862708
            ],
            [
              -97.7376175,
              30.2862752
            ],
            [
              -97.7376155,
              30.2863024
            ],
            [
              -97.7376002,
              30.2864981
            ],
            [
              -97.7380471,
              30.2865384
            ],
            [
              -97.738326,
              30.286557
            ],
            [
              -97.7382777,
              30.2872101
            ]
          ],
          [
            [
              -97.737561,
              30.2867608
            ],
            [
              -97.73755,
              30.2868706
            ],
            [
              -97.7375714,
              30.2868722
            ],
            [
              -97.7375675,
              30.2869108
            ],
            [
              -97.7375647,
              30.2869391
            ],
            [
              -97.7377177,
              30.28695
            ],
            [
              -97.7377251,
              30.2868806
            ],
            [
              -97.7378988,
              30.2868933
            ],
            [
              -97.7378909,
              30.2869626
            ],
            [
              -97.7380413,
              30.2869745
            ],
            [
              -97.7380505,
              30.2868831
            ],
            [
              -97.7380677,
              30.2868844
            ],
            [
              -97.7380814,
              30.2867475
            ],
            [
              -97.7380864,
              30.2866972
            ],
            [
              -97.7380525,
              30.2866947
            ],
            [
              -97.7375712,
              30.2866587
            ],
            [
              -97.737561,
              30.2867608
            ]
          ]
        ],
        "type": "Polygon"
      },
      "id": "0",
      "properties": {
        "access_roo": null,
        "addr_house": "105",
        "addr_stree": "East 24th Street",
        "building": "university",
        "building_m": null,
        "name": "Robert A. Welch Hall",
        "osm_id": "227077",
        "osm_way_id": null,
        "roof_mater": null
      },
      "type": "Feature"
    }
  ]
}
```
