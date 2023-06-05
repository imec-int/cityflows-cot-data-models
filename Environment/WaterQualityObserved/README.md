# WaterQuality Data Models

This directory contains the Water Quality measurement data model specification used for the Internet of Water project. The models are specified through json schemas.

The models are based on Fiware models, as specified in their [Github repo](https://github.com/smart-data-models/dataModel.WaterQuality/tree/master).

To specify an WaterQuality measurement the WaterQualityObserved json schema is used.

## Date fields

All date fields, including `dateObserved`, should be encoded in the same, ISO8601 compliant, format:

```
YYYY-MM-DDTHH:MM:SSZ
```

This means they should always be represented in the UTC timezone, have a second specification, but no milisecond specification. This makes parsing of the date field a much simpler string operation, instead of having to parse the field according to the ISO standard, which is a much more expensive operation. An example date is `2021-05-04T16:47:59Z`.

The timezone indication MUST be done with a trailing `Z` (which is allowed by the ISO standard), nor should any of the separators (`-`, `T`, `:`) be replaced of omitted, even if the ISO standard allows for this.

## Supported water quality parameters

Below are all currently supported parameters and the units in which they should be communicated. The unit code should explicitely be provided as metadata in the field `unitCode`.

|  Property Name                         | Fiware code  | Full name                     | abbrev | Unit              | UN unit     |
| -------------------------------------- | ------------ | ----------------------------- | ------ |------------------ | ----------- |
| temperature                            | temperature  |                               |        | °C                | CEL         |
| conductivity<sup>[1](#footnote1)</sup> | conductivity |                               |        | µS/cm             | G42         |
| pH                                     | pH           | Acidity / Alkalinity          | pH     | pH                | Q30         |
| depth<sup>[2](#footnote2)</sup>        |              |                               |        | mm H<sub>2</sub>O | HP          |
| batteryLevel<sup>[3](#footnote3)</sup> |              |                               |        |                   |             |
| deviceTemperature                      |              |                               |        | °C                | CEL         |
| deviceHumidity                         |              |                               |        | %                 | P1          |

The full list of UN codes can be found [here](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
See also [fiware waterqualityobserved model](https://fiware-datamodels.readthedocs.io/en/test_next_version/Environment/WaterQualityObserved/doc/spec/index.html)

## Water Quality Sensors

Models for the water quality sensors are specified in the devices directory

## Footnotes

<a name="footnote1">1</a>: Conductivity SHOULD NOT be temperature corrected.  
<a name="footnote2">2</a>: Depth should be based on (hydraulic) pressure measured by the sensor and is preferrably corrected for atmospheric pressure before being transformed into a depth in mm. Note that pressure sensors with a vented tube are automatically corrected for atmospheric pressure (as they basically measure a pressure difference between the sensor and the surface). Alternativelly, meteorological data could be used to correct for atmospheric pressure. Also, depth measured by hand during installation of the sensor should not be used for this field. For this, update the `sampling point` in the location database.  
<a name="footnote3">3</a>: Battery level is indicated as a fraction between 0 and 1, where 0 is empty and 1 is full. There is no unit code for this. Transformation of battery voltage to battery level is very device and battery specific and therefore should be done by the device operator. It is possible to add the actual measured battery voltage as metadata, in the `rawValue` field. In that case, the metadata field `rawValueUnitCode` should be set to `2Z`, meaning battery voltage is measured/communicated in mV.  
