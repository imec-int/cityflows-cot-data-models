# Device Data Models

This directory  contains all the device data model specification used for City of Things (CoT) projects. The models are specified through json schemas.

The models are based on fiware models, as specified in https://github.com/FIWARE/dataModels/tree/master/specs/Device

To specify a device, two models are used:

- DeviceModel
- Device

*DeviceModels* model a class of sensors (eg Fixed air quality sensors), whereas a *Device* is a specific sensor (eg VMM_T2H801_Zwijndrecht) .

For each domain, type of sensor a directory will specify the device models for the sensors used. Currently the following domains have been identified

- WaterLevel Sensors
- Air Quality
