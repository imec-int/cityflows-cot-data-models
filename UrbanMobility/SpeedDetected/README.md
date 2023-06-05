# SpeedRadar Data Model

This directory contains the *SpeedRadar* measurement data model specification used for City of Things (CoT) projects. The models are specified through json schemas. To specify a speed detection measurement the `SpeedDetected` json schema is used.

As there is no fiware model for speed detection, a model, based on fiware models, as specified in the <https://github.com/FIWARE/dataModels/tree/master/specs/> set of json schema specifications, has been created.

## Supported Measurands

Currently only the *velocity* (speed in m/s) is measured. The device specification will specify the location and heading of the measurement.

## SpeedRadar Sensor

A model for the SpeedRadar sensor is specified in the devices directory.