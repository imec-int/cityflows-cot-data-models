# AirQuality Data Models

This directory  contains the Air Quality measurement data model specification used for City of Things (CoT) projects. The models are specified through json schemas.

The models are based on fiware models, as specified in https://github.com/FIWARE/dataModels/tree/master/specs/Device

To specify an AirQuality measurement the AirQualityObserved json schema is used.

## Supported Measurands

Curently the following measurands are supported:

- PM1
- PM25
- PM10
- O3
- NO2
- temperature
- humidity

## Raw vs Calibrated Measurement

External applications are mainly interested in the calibrateded value for a measured properties. For internal purposes, the raw values remain relevant for the development and improvement of the calibration algorithms. Moreover, IMEC does not want to export both as this would expose IMEC's IP on air quality calibration. Therefore, raw values shall be stored as metadata, that is not exposed. An example of this is described here:

```javascript
"NO": 100,
"O3": 39000,
...
  "metadata": {
    "NO": 99.41021,
    "O3": 39211,
    ...
}
```

## Air Quality Sensors

models for the air quality sensors are specified in the devices directory

