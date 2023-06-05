# SpeedRadar Detector Data Model

This directory contains the SpeedRadar Detector specification used for City of Things (CoT projects. The model is specified through json schemas.

As there is no specific fiware model for speed detection devices, a model, based on fiware models, as specified in https://github.com/FIWARE/dataModels/tree/master/specs/devices has been used.

The key paramneter for these devices is their

- **location**; where is it based, potentially with a address description;
- **heading**; in which direction is the detector pointing

Detections using these devices will use the model defined in the SpeedDetected directory, part of UrbanMobility.


