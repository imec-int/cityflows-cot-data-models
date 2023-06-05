# Cityflows Data Model

This directory contains the *CityFlows* data model specification used for City of Things (CoT) . The models are specified through json schemas. The data model is based on the [FiWare Traffic Flow Observed specification](https://fiware-datamodels.readthedocs.io/en/latest/Transportation/TrafficFlowObserved/doc/spec/index.html), extending it to allow both intensity and flow direction in a specified geographical area, as well as indication the accuracy of the data source and the method of data aggregation.

The main output of the cityflows data aggregation model are people counts together with a traffic flow, expressed per modality, for street segments. Pedestrians are also treated as a specific modality. Input can also be viewed as a traffic flow, although not necessarily in streets, but in larger or smaller areas. The input stream can carry several modalities at once while the output aims to provide streams split up for each modality. 

This document aims to provide information for
1.  a smooth integration of input sources, ready to be fed into the CityFlows
    service.
2.  a standardized representation of output of Cityflows, ready to be ingested
    by other services.



## Changed data fields

-   `vehicleType` : based on the 'vehicleType' field from the TrafficFlowObserved classification, but also allows pedestrians and multimodal values. There is also an 'stationary' modality meant to represent the people that are not moving in the model.

## Added data fields

-   `location` : this field indicates the exact (virtual) location where an IoT device is present.
-   `refRoadSegment`: relationship pointing to a concerned road segment where the observation has been made. In our case, this will point to the [Wegenregister from the Flemish Region](https://overheid.vlaanderen.be/informatie-vlaanderen/producten-diensten/wegenregister). We point to the *WS_OIDN*, the unique id of a road segment.
-   `area_covered` : the main difference with the already existing geo-inspired location fields, is that this new  field can be as wide or narrow as desired, and more importantly independent from the local street geometry context.  Location of a traffic flow observation must represented by a
GeoJSON geometry. This can be a Polygon or LineString object. LineStrings can be used to model streets, Polygons can be used to indicate the range area of certain IoT devices.
-   `direction`: 
    -   `heading`: used to describe the bearing in degrees (0 - 359) of the street segment. Bearing 90 would indicate a West to East street. The bearing of a street segment can be calculated using a straight line from the first to last point of the street. Mandatory if flow_up and/or flow_down is provided to ensure self-explanatory data.
    -   `flow_up`: used to describe the amount of traffic moving in 
      the direction of the street, as described by the `heading` variable.
    -   `flow_down`: used to describe the amount of traffic moving in 
      the opposite direction of the street, as described by the `heading` variable.
-   `measurement_type`: this specifies the way in which data is collected. Depending on the method used, data can be collected in various ways. We differentiate between: 
    - `snapshot`: this indicates that within the area and within a speciif moment within the interval, an instanteneous count was made. Example: Proximus telco data.
    - `point_measurement` (aggregated) counting is done at a very specific location, and thus the `area_covered` field is not well suited to handle the situation. Instead, average speeds should be given to allow the calculation of a correct density. Example: Telraam data.
    - `unique_counts` (aggregated): counts within the area are done, unique entities are counted only once within the set timeframe. Example: citymesh:
    - `non_unique_counts` (aggregated) :
-   `accuracy`: this number is an indication of the noise range around the measured values.

For a more detailed explanation, see the specs.

## Location data in geoJSON format
The geolocation of the data source, the `area_covered` in the above table, is a very important piece of data to make sure the counts are allocated to the correct geometric location. Coordinates must be provided in WSG84 format (GPS coordinates)

### Creating a GeoJSON
A simple GeoJSON can be created using the website [geojson.io](http://www.geojson.io), where you can manually select a polygon indication the area(s) being measured by a certain data source.

### Some examples
A camera with a 110° viewing angle and a 50 meter detection range could result in a GeoJSON like this:
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              4.39701497554779,
              51.21500084275859
            ],
            [
              4.396730661392212,
              51.215175576472404
            ],
            [
              4.396698474884033,
              51.21514533414631
            ],
            [
              4.39665824174881,
              51.21509997061995
            ],
            [
              4.396628737449646,
              51.21504788651601
            ],
            [
              4.396618008613586,
              51.21496387977265
            ],
            [
              4.396668970584869,
              51.21487987287598
            ],
            [
              4.396722614765167,
              51.214822748098705
            ],
            [
              4.3968164920806885,
              51.21479418568347
            ],
            [
              4.39701497554779,
              51.21500084275859
            ]
          ]
        ]
      }
    }
  ]
}
```

A bluetooth scanner in a certain street segment would look something like this:
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              4.397800862789154,
              51.21605763557773
            ],
            [
              4.397500455379486,
              51.21569977363505
            ],
            [
              4.397672116756438,
              51.2156695316533
            ],
            [
              4.397961795330048,
              51.216008912753814
            ],
            [
              4.397800862789154,
              51.21605763557773
            ]
          ]
        ]
      }
    }
  ]
}
```
