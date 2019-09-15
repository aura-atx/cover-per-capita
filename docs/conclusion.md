# Conclusion

## Acronyms

* ODP: Open Data Portal
* OSM: Open Street Map
* TCAD: Travis County Appraisal Database

## 2019-09-15 - First iteration

This is the first iteration of our research regarding impervious cover per capita.

To compile this data set, we used the TCAD database and the OSM data set for the city of Austin, TX.

### Results

Entries: 569 (~ about 1/1000 of the buildings in the city)

| Type         | Impervious cover | Count      |
|--------------|------------------|------------|
| apartments   | 36.76%           |         20 |
| church       | 35.89%           |          1 |
| college      | 52.27%           |          1 |
| commercial   | 26.03%           |         29 |
| detached     | 24.53%           |         73 |
| hospital     | 18.76%           |          3 |
| house        | 32.55%           |        377 |
| industrial   | 58.52%           |          1 |
| kindergarten | 52.04%           |          1 |
| office       | 44.17%           |          2 |
| public       | 6.05%            |          1 |
| residential  | 27.11%           |          4 |
| retail       | 17.87%           |         14 |
| roof         | 7.12%            |          4 |
| school       | 15.36%           |         18 |
| university   | 53.68%           |          2 |

### Problems and limitations

We were not able to find the number of occupants per building. The closest we could get was using census tracts, but the smallest tract represents at least a couple of blocks (usually 20-40 properties).

The school system also supposedly provides data regarding their attendance, but we were not able to find this information.

The TCAD database is not model either. It does not contain the type of building, nor the its footprint. The quality of the data is questionable. For instance the acreage is not always provided with the same unit, or uses a specific way to shorten the street names.

The OSM data contains the type of a building, but only 2604 entries are tagged correctly.

The ODP provides a building footprint data set, but there is no way to join it with any other data set which made it unsable.

### Potential improvements

* Find a way to programmatically query the TCAD database.
* Improve the `normalize_suffix` function to increase the number of exact matches to join the TCAD and the OSM data sets.
* Find a way to use the ODP building footprint data set.
* Find a way to retrieve the number of occupants per building
