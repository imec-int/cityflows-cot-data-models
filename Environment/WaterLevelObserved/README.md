# WaterLevelObserved Data Models

This directory  contains all the WaterLevelObserved data model specification used for City of Things (CoT) projects. 
The models are specified through json schemas.

There is no fiware model for WaterLevel measurement, so the models follow the same principle as other fiware models, as specified in https://github.com/FIWARE/dataModels/tree/master/specs/Device

A WaterLevel measurement uses the WaterLevelObserved.json schema

## WaterLevel Sensors

The specification of the WaterLevel sensors can be found in the Devices directory.

## Pluvio

The rain gauge sensors will report their measurements using the WeatherObserved data model (https://github.com/FIWARE/dataModels/tree/master/specs/Weather/WeatherObserved). The "precipitation" field will be used for that purpose.