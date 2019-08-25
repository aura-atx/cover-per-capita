# Open Street Map

## Evaluation

**Source**: Shapefiles for the city of Austin, TX were generated why the [HOT Export](https://export.hotosm.org/en/v3/) online service, then converted to GeoJSON using [Fiona](https://pypi.org/project/Fiona/).

### Relevant data

| Property | Description |
|---|---|
|entry count| 447820|
|building| building type ([OSM Key:building](https://wiki.openstreetmap.org/wiki/Key:building))|
|geometry| shape of a building (Note that OSM allows multipolygon structures)|

### Other findings

The `building` property has 89 possible values, but we could limit our search to only a few types like `house` and
`appartments`. This provides us with 703 entries for appartments, and 4945 entries for houses.

```bash
$ jq '[ .features[] | select(.properties.building == "house")] |length' austin-tx_planet_osm_polygon_polygons.json
703
$ jq '[ .features[] | select(.properties.building == "apartments")] |length' austin-tx_planet_osm_polygon_polygons.json
4945
```

I am not sure how to programatically regenerate the data set.

### Feature example

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
