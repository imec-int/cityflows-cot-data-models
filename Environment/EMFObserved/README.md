# EMV Data Models

This directory  contains  the EMFObserved data model specification used for City of Things (CoT) projects.
The models are specified through json schemas.

There is no fiware model for ElectroMagmetic Field measurement, so the models follow the same principle as other fiware models, as specified in <https://github.com/FIWARE/dataModels/tree/master/specs/Device>

A EMF measurement uses the EMFObserved.json schema

## EMF Structure

EMF is measured for different frequencies. For each frequency the following values will be measured:

- minimum value
- average value
- maximum value

In json this will look like

```javascript
{
    ...
    "frequency": "900",
    "min": 0,
    "avg": 20,
    "max": 50,
    ...
}
```

Currently the following frequencies are supported: 900, 180, 2100, 2400 MHz

The reported values are the root-mean-squared (RMS) electrical field strength(“Erms” of “E_RMS”), and measured in V/m (UNECE/CEFACT D50)

## EMV Sensors

The specification of the EMF sensor can be found in the Devices directory.
