# Traffic flow observed - extension

## Description

An observation of traffic flow conditions at a certain place and time. This
entity is primarily associated with the Automotive and Smart City vertical
segments and related IoT applications. This format is an extension of the [FiWare Traffic Flow Observed format](https://fiware-datamodels.readthedocs.io/en/latest/Transportation/TrafficFlowObserved/doc/spec/index.html). We only describe the added or slightly modified fields.

## Data Model

The data model is defined as shown below:

-   `vehicleType` : this field is based on the 'vehicleType' field from the TrafficFlowObserved classification. It takes all the allowed vehicles there, but it can take a few additional values:
    -   See definition at [Vehicle](https://github.com/FIWARE/dataModels/blob/master/specs/Transportation/Vehicle/Vehicle/doc/spec.md).
    -   Additional allowed values: **'pedestrian'**, **'stationary'**
    -   Allows multiple values, to denote a potential heterogeneous traffic stream
    -   Optional
    
-   `location` : Location of this traffic flow observation represented by a
    GeoJSON geometry. The location points to the source of the measuring device or to the center of the 'area_covered' by the (virtual) device.

    -   Attribute type: `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory if `refRoadSegment` is not present.
    -   This GeoJSON must be a Point.

-   `refRoadSegment`: relationship pointing to a concerned road segment where the observation has been made.
    -   Attribute type: Relationship
    -   Normative references: [Wegenregister from the Flemish Region](https://overheid.vlaanderen.be/informatie-vlaanderen/producten-diensten/wegenregister)
    -   Format: uri

-   `area_covered` : Location of this traffic flow observation represented by a
    GeoJSON geometry. The area_covered points either to a line segment corresponding to a road, or a polygon indicating the geographical range of the data.

    -   Attribute type: `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory if `refRoadSegment` is not present.
    -   This GeoJSON must be a Linestring or Polygon.

-   `direction`: used to describe the direction in which traffic is moving, represented by a triple of entities:
    -   `bearing`: used to give the direction of traffic as a bearing between 0 and 359 degrees.
        -   Attribute type: [Number](https://schema.org/Number)
        -   Default unit: degrees
        -   "minimum": 0
        -   "maximum": 359
        -   Optional

    -   `flow_up`: used to describe the amount of traffic moving in the
        the direction of the street, following the coordinates as they are given. (extension)
        -   Attribute type: [Number](https://schema.org/Number)
        -   Default unit: people
        -   Optional

    -   `flow_down`: used to describe the amount of traffic moving in the
        the opposite direction direction as magnitude_flow_up (extension)
        -   Attribute type: [Number](https://schema.org/Number)
        -   Default unit: people
        -   Optional

-   `measurement_type`: used to describe the kind of measurement (methodology of capturing counts).
    -   Attribute type: Property, string
    -   Allowed values: `snapshot`, `point_measurement`, `unique_counts`
    -   If nothing is specified, `unique counts` is assumed
    -   Optional

-   `accuracy`: this number is an indication of the noise around the measured values (extension)
    -   Attribute type: [Number](https://schema.org/Number)
    -   Default unit: percentage
    -   Optional

**Note**: JSON Schemas only capture the NGSI simplified representation, this
means that to test the JSON schema examples with a
[FIWARE NGSI version 2](http://fiware.github.io/specifications/ngsiv2/stable)
API implementation, you need to use the `keyValues` mode (`options=keyValues`).

## Examples

### Normalized Example (input)

Normalized NGSI response
Provides fictional 10 minute data counting 197 people in a square polygon located in the Antwerp City region.

**In the NGSI-LD standard**
```json
{
    "id": "TrafficFlowObserved-Valladolid-osm-60821110",
    "type": "TrafficFlowObserved",
    "dateObserved": {
        "type": "Property",
        "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"
    },
    
    "dateObserved": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2019-06-07T11:10:00Z"
        }
    },
    
    "dateObservedFrom": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2019-06-07T11:10:00Z"
        }
    },
 
    "dateObservedTo": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2019-06-07T11:20:00Z"
        }
    },
        "intensity": {
        "type": "Property",
        "value": 197
    },
    
    "vehicleType": [
            {
            "type": "Property",
            "value": "car"
            },
            {
            "type": "Property",
            "value": "lorry"
            }
        ]
    },
 
    "area_covered": {
        "type": "GeoProperty",
        "value": {
            "type": "Polygon",
            "coordinates": [
          [
            [
              4.4088371,
              51.22333507
            ],
            [
              4.40883553,
              51.22153739
            ],
            [
              4.40597283,
              51.22153835
            ],
            [
              4.40597283,
              51.22153835
            ],
            [
              4.40597429,
              51.22333602
            ]
          ]
        ]        }
    },

    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [
          
            [
              4.40740418,
              51.22243718
            ]
          ]
                }
    },

    "@context": [
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",
        "https://schema.lab.fiware.org/ld/context"
    ]
}
```

**In the NGSIv2 standard**
```json
{
    "id": "TrafficFlowObserved-cityflows-60821110",
    "type": "TrafficFlowObserved",
    "dateObserved": {
        "type": "Property",
        "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"
    },
    
    "dateObserved": {
        "type": "DateTime",
        "value": "2019-06-07T11:10:00Z"
    },

    "dateObservedFrom": {
        "type": "DateTime",
        "value": "2019-06-07T11:10:00Z"
    },
 
    "dateObservedTo": {
        "type": "DateTime",
        "value": "2019-06-07T11:20:00Z"
    },
    
    "intensity": {
        "type": "Number",
        "value": 197
    },
    
    "vehicleType": [
            {
            "type": "Property",
            "value": "car"
            },
            {
            "type": "Property",
            "value": "lorry"
            }
        ]
    },
 
    "area_covered": {
        "type": "geo:json",
        "value": {
            "type": "Polygon",
            "coordinates": [
          [
            [
              4.4088371,
              51.22333507
            ],
            [
              4.40883553,
              51.22153739
            ],
            [
              4.40597283,
              51.22153835
            ],
            [
              4.40597283,
              51.22153835
            ],
            [
              4.40597429,
              51.22333602
            ]
          ]
        ]        }
    },

    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [
          
            [
              4.40740418,
              51.22243718
            ]
          ]
                }
    },
}
```

### Normalized example (output)
The following example gives an output for bicycle flows in a certain line segment (representing a street segment), where 50 people are to be expected and 20 people will move heading West.

**In the NGSI-LD standard**

```json
{
    "id": "urn:ngsi-ld:TrafficFlowObserved:TrafficFlowObserved-Valladolid-osm-60821110",
    "type": "Cityflows",
    "dateObserved": {
        "type": "Property",
        "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"
    },
    
    "dateObserved": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2019-06-07T11:10:00Z"
        }
    },
    
    "dateObservedFrom": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2019-06-07T11:10:00Z"
        }
    },
 
    "dateObservedTo": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2019-06-07T11:20:00Z"
        }
    },
 
    "intensity": {
        "type": "Property",
        "value": 50
    },
    
    "vehicleType": {
        "type": "Property",
        "value": "bicycle"
    },
 
 
    "direction": {
        "type": "Property",
        "value": 270
    },
 
 
    "flow_up": {
        "type": "Property",
        "value": 20
    },
 
 
    "accuracy": {
        "type": "Property",
        "value": 0.9
    },
 
 
    "area_covered": {
            "type": "LineString",
            "coordinates": [
            [
                4.412185549736023,
                51.21823498913796
            ],
            [
                4.411466717720032,
                51.218053546941015
            ],
            [
                4.411230683326721,
                51.218033386652785
            ],
            [
                4.410490393638611,
                51.218043466797994
            ],
            [
                4.410286545753479,
                51.218043466797994
            ]
        ]
        
    },
 
    "address": { 
        "type": "PostalAddress", 
        "value": { 
            "addressLocality": "Antwerpen", 
            "addressCountry": "BE", 
            "streetAddress": "Meir" 
        } 
    },

    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [
          
            [
              4.40754532,
              51.218134
            ]
          ]
                }
    },

    "@context": [
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",
        "https://schema.lab.fiware.org/ld/context"
    ]
}
```

**In the NGSIv2 standard**

```json
{
    "id": "TrafficFlowObserved--60821110",
    "type": "Cityflows",
    "dateObserved": {
        "type": "Property",
        "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"
    },
    
    "dateObserved": {
        "type": "DateTime",
        "value": "2019-06-07T11:10:00Z"
    },
    
    "dateObservedFrom": {
        "type": "DateTime",
        "value": "2019-06-07T11:10:00Z"
    },
 
    "dateObservedTo": {
        "type": "DateTime",
        "value": "2019-06-07T11:20:00Z"
    },
 
    "intensity": {
        "type": "Number",
        "value": 50
    },
    
    "vehicleType": {
        "type": "Property",
        "value": "bicycle"
    },
 
 
    "direction": {
        "type": "Number",
        "value": 270
    },
 
 
    "flow_up": {
        "type": "Number",
        "value": 20
    },
 
 
    "accuracy": {
        "type": "Number",
        "value": 0.9
    },
 
 
    "area_covered": {
        "type": "geojson",
        "value": {
            "type": "LineString",
            "coordinates": [
            [
                4.412185549736023,
                51.21823498913796
            ],
            [
                4.411466717720032,
                51.218053546941015
            ],
            [
                4.411230683326721,
                51.218033386652785
            ],
            [
                4.410490393638611,
                51.218043466797994
            ],
            [
                4.410286545753479,
                51.218043466797994
            ]
        ]
        }
    },
 
    "address": { 
        "type": "PostalAddress", 
        "value": { 
            "addressLocality": "Antwerpen", 
            "addressCountry": "BE", 
            "streetAddress": "Meir" 
        } 
    },

    "location": {
        "type": "geojson",
        "value": {
            "type": "Point",
            "coordinates": [
          
            [
              4.40754532,
              51.218134
            ]
          ]
                }
    },
}
```

### key-value pairs Example (To update)

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "TrafficFlowObserved-Valladolid-osm-60821110",
    "type": "TrafficFlowObserved",
    "laneId": 1,
    "address": {
        "streetAddress": "Avenida de Salamanca",
        "addressLocality": "Valladolid",
        "addressCountry": "ES"
    },
    "location": {
        "type": "LineString",
        "coordinates": [
            [-4.73735395519672, 41.6538181849672],
            [-4.73414858659993, 41.6600594193478],
            [-4.73447575302641, 41.659585195093]
        ]
    },
    "dateObserved": "2016-12-07T11:10:00",
    "dateObservedFrom": "2016-12-07T11:10:00Z",
    "dateObservedTo": "2016-12-07T11:15:00Z",
    "averageHeadwayTime": 0.5,
    "intensity": 197,
    "occupancy": 0.76,
    "averageVehicleSpeed": 52.6,
    "averageVehicleLength": 9.87,
    "reversedLane": false,
    "laneDirection": "forward"
}
```
## Use it with a real service

T.B.D.

## Open issues
