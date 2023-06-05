# Water Quality Verified

## Description

Water Quality Verified data model for IoW is intended to represent water quality parameters 
at a certain water mass: surface water, sewer or groundwater enriched with flags defined
by running quality checks against the incoming sensor data.

The data model is an extension on top of the WaterQaulityObserved, adding metadata flags for each of the observations. These flags assign a Boolean value to define the value respectively valid (True) or not-valid (False) according to a given algorithm. A measured value can have a mix of flags and its up to the client to decide what tot do with the combination of data quality check flags.

In this specification, only the __differences__ with the `WaterQualityObserved` model are specified, with respect to both the attributes as the metadata. Existing attributes and metadata fields in the `WaterQualityObserved` model not specified here, are part of the data model as well.

## Data model

A JSON Schema corresponding to this data model can be found [here](../schema.json).

-   `id` : Unique identifier. It shall be a URN in the form
    `urn:ngsi-v2:be:imec:cot:WaterQualityVerified:<identifier>` where `<identifier>` shall be a 
    unique ID string.

-   `type` : Entity type. It must be equal to `WaterQualityVerified`.

-   `refDevice` : Reference to the IoW Sensor Devices, both the reference to the `WaterQualityDevice` as well as the `WaterQualityVerificationDevice`.
    -   Attribute type: `Relationship`. Reference to an entity of type `Device` and `WaterQualityVerificationDevice`
    -   Mandatory


### Water quality parameters

The following metadata fields are additional metadata fields for each of the water quality parameters defined in the `WaterQualityObserved` data model. 

__Note:__ _Configuration values_ mentioned are defined on the (virtual) device level.

-   Attribute metadata:
    -  `flag_minmax`: The flag resulting from a min-max bound check. If the value is outside the given configuration min/max boundary values, a False is returned, otherwise True.
        -   Type: [Boolean](https://schema.org/Boolean)
        -   Optional
    -  `flag_jump`: The flag resulting from a jump check. If the jump from this value with the previous value is larger than a given configuration value, a False is returned, otherwise True.
        -   Type: [Boolean](https://schema.org/Boolean)
        -   Optional
    -  `flag_zscore`: The flag resulting from a z-score check. If the value is outside the given z-score configuration value boundaries, a False is returned, otherwise True.
        -   Type: [Boolean](https://schema.org/Boolean)
        -   Optional
    -  `flag_stationary`: The flag resulting from a stationary check. If the value is part of a set of values that do not change (within a given configuration value)for a given configuration period, a False is returned, otherwise True.
        -   Type: [Boolean](https://schema.org/Boolean)
        -   Optional

    
## Use it with a real service

See [Use case validation](https://git.vito.be/projects/IOW/repos/usecase_validation/browse).

## Open Issues

-   Store the data quality settings in a separate device, linked with `refDevice` or can we add these as a separate attribute to the actual `Device` model of IoW? Both have advantages.

A quick draft example on how the Device could look like:

```
{
  "id": "urn:ngsi-ld:deviceWaterQualityObservedDataQuality:iow:1",
  "type": "Device",
  "category": ["implement"],
  "controlledProperty": ["dataQuality"],
  "controlledAsset": ["urn:ngsi-ld:WaterQualityObserved:iow:1"],
  "ipAddress": ["192.14.56.78"],  # Change to an URL to which the data can be POST by broker
  "refDeviceModel": "device-waterqaulityobserved-dataquality-iow",
  "deviceState": "ok",
  "dateFirstUsed": "2019-09-11T11:00:00Z",
  "softwareVersion": "https://github.com/iow/dataquality/releases/tag/v0.3.1"  # link to the release tag of algorithm module,
  "configuration": {
      "lag_time": 12                 # number of hours lag time the flags are released for a given measurement
      "flag_min_max": [4., 8.],      # min and max boundaries
      "flag_jump": [7.],             # absolute value of maximum jump
      "flag_zscore": [3],            # Z-score
      "flag_stationary": [0.2, 300], # tolerance and duration
    },
}
```


