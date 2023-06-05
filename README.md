# City of Things Data Models

This repository contains all the data model specification used for City of Things (CoT) projects. The models are specified through json schemas.

The specifications are ordered by domain in the different directories:

- Device
- WaterLevel
- AirQuality
- SpeedRadar

The models are based on fiware models, as specified in https://github.com/FIWARE/dataModels.

The data specifications in this repo are designed for the Cityflows model as it was built for the City of Things project. Further iterations on these data formats might be documented in other repositories.

## Concept

The models defined here are based on the following assumptions

- Device models are to be used to store information (ie metadata) for sensors, actuators, or similar
- The measurements from sensors are captured using models for eg AirQuality, WaterLevel or others
- Device are based on DeviceModels. For some of the sensors these models are defined

For each domain (eg flooding), 

1. the DeviceModels for the relevant devices(sensors) need to be added to the Orion Context Broker. Subsequently, 
2. each device needs to added, with their relevant characteristics(properties)
3. Measurements are then added, referring to these devices. The metadata is then added through an update of the Device
4. Each measurement and device added to the Orion broker shall use the same *"source"* property. For the flooding project all device/measurement shall use "cot.flooding".

```javascript
    "source": "cot.flooding"
```

### Location Coding

The fiware data models are using geoJSON to specify a location. In our current implementation, we use geohash for locations. The able to keep this information, the proposal is to use a top level attribute "geohash" field for this.

```javascript
"location":{
        "type": "Point",
        "coordinates": [4.42869404,51.25484965]
}
"geohash": "u155sf8vh"
 ```

This repository is structured following the FIWARE data model structure

## Environment

Contains the `WaterLevelObserved` and `AirQualityObserved` models

## Testing

Contains models for testing the proper operation of the CoT stack

## Device
Schema and models for devices, typically all the deployed sensors 

- Airquality sensors
- Waterlevel sensor
- Speedradar sensor

## Urban Mobilitty

Schema for SpeedRadar measurements.

