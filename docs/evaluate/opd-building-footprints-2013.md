# Building Footprints Year 2013

**Source**: Austin Open Data Portal --
https://data.austintexas.gov/Locations-and-Maps/Building-Footprints-Year-2013/7bns-7teg

## Evaluation

The GeoJSON data set was used for this evaluation.

### Relevant data

| Property | Description |
|---|---|
|entry count| 585916|
|max_height|height of a building in feet|
|geometry| shape of a building|

### Other findings

Other than that, the data set is not very useful:

* All the buildings are of type "Structure".
  * Based on the definition of a High rise: 12 stories / 35m / 155 ft
  ([Skyscraperpage](https://skyscraperpage.com/site/faq/#2),
  [Wikipedia](https://en.wikipedia.org/wiki/High-rise_building)), we could be able to the categorize each entry in
  "High rise" or "Non high rise", but that's pretty much it.

### Feature example

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
