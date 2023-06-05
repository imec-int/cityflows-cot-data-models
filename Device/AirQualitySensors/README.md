# Device Data Models

## AirQuality Sensors

This directory contain models for the following sensors:

- imec Sensors, used as fixed, amd mobile sensor
  - imec-airquality-fixed-sensor.json
  - imec-airquality-mobile-sensor.json  

- VMM Sensors, used as reference sensors
  - vmm-airquality-sensor.json

- Calibration Device
  - imec-airquality-calibration-devicemodel.json
  - AirQualityCalibrationDevice.json

## Calibration

The airquality measurements coming from imec sensors needs to be calibrated in order for them to provide useful data. This calibration process works as follows:

1. The calibration application (CA) subscribes to new measurements in Orion
2. a sensor publishes a measurement to the Orion Context Broker
3. This new measurement is published to the CA
4. The CA reads calibration parameters from the associated calibration device, and outputs the calibrated  values to Orion
5. Once a day the calibration parameters for a device are updated based on data stored in the historical database.

### Calibration Device

A virtual device has been defined to capture the parameters used for the calibration of raw air quality measurements. The main reason for this is that, for IP reasons, we want to limit access to raw data and calibration parameters. 

- All calibrated data and information on raw devices will be published as open public data;
- Whereas the raw data and the calibration parameters are only accessible to select user groups. 

As this is not a physical device, there are a few differences compared to _regular_ devices:

1. the `controlledAsset` property refers to the actual air quality device it calibrates;
2. `dateLastCalibration` will be updated after every update run (see 5. above);
3. They do not have a `location` property;
4. The contain an object `calibrationParameters` to capture these.

#### Calibration Parameter Structure
These are stuctured as follows

``` javascript
"calibrationParameters": {
    "type": "array",
    "items": {
    "measurand": {
        "type": "string"
    },
    "type": "array",
    "items": [ 
        {
        "type": "string"
        }, 
        {
        "type": "number"
        }
    ]
}
```

`measurand` is the property to be calibrated, e.g, PM10. For each of these an array of tuples defines the parameters, as can be seen in the example:

```javascript
"calibrationParameters": [
    {
    "measurand": "PM10",
    "values": [
        ["alpha_temp1", 0]
        ["alpha_temp0", 1.4748245749299949],
        ["alpha_hum1", 0],
        ["alpha_hum0", 0.4274332746019941],
        ["beta_raw", -45.12147488204749],
        ["alpha_lin_raw", 3.299582829185965e-13],
        ["alpha_log_raw", 10.083159838834138]
    ]
    },
    {
    "measurand": "NO2",
    "values": [
        ["alpha_temp2", 0],
        ["alpha_temp1", 0],
        ["alpha_temp0", 0.4173273165306822],
        ["alpha_hum2", 0],
        ["alpha_hum1", 1.1447191135266566],
        ["alpha_hum0", -1.394444277509778],
        ["beta_raw", -1.4032166366600107],
        ["alpha_raw", 0.6594466427579307]
    ]
    } 
]
```

## Supported Measurands

Curently the following measurands are supported:

- PM1
- PM25
- PM10
- O3
- NO2
- temperature
- humidity

Note: Currently only PM25, P10, and NO2 can be calibrated.

## Mobile Sensors

When a measurement has been received from a mobile sensor, also the location of the device(sensor) needs to be updated.
=======
When a measurement has been recieved from a mobile sensor, also the location of the device(sensor) needs to be updated.

## Test Devices

Test devices are used to monitor proper operation of the CoT stack. There are two possible approaches: 
 - Stess testing: sending as many messages through as possible to the agent in a limited amount of time and test if all messages have come through
 - Happy path testing: monitoring that messages are properly processed on a continuous basis
