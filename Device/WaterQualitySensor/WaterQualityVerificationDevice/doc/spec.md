# Water Quality Verification Device

## Description

An virtual Device intended to check the data quality of a given `waterQualityObserved` or `waterQualityCalibrated` measurement 
according to a set of quality check algorithms.

## Data Model

The data model is defined as shown below:

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `WaterQualityVerificationDevice`.

-   `controlledAsset` : Refers to the device identifier (uri) of the WaterQualitySensor (the device), in the form `urn:ngsi-v2:be:imec:cot:WaterQualityDevice:<identifier>`
    -   Attribute type: `Relationship`. Reference to an entity of type `Device`.
    -   Mandatory


-   `controlledProperty` : a list of observed parameters which are verified by the device (e.g. pH, temperature, conductivity etc...)
     - Attribute type : List of [Text](https://schema.org/Text)
     - Mandatory


-   `source` : refers to the entity type on which the verification is run, can be either `WaterQualityObserved` or `WaterQualityCalibrated`         -   Mandatory
 
-    `refDevice` : Reference to the IoW Sensor Device `waterQualityDevice` (__NOTE__ : not sure if required, is same as controlledAsset)
    -   Attribute type: `Relationship`. Reference to an entity of type `Device`.
    -   Mandatory

-   `category` : Equal to `implement`. Optional but recommended to optimize queries.

-   `ipAddress` : The IP address or URL of the virtual device on which measurements to check are received. It can be a comma separated list
    of values if the device has more than one IP address.

    -   Attribute type: Property. List of [Text](https://schema.org/Text) or [URL](https://schema.org/URL)
    -   Optional

-   `configuration` : Device's technical configuration. This attribute is
    intended to be a dictionary of properties which capture parameters which
    have to do with the configuration of each of the data quality checks. 
    For a full description of the dictionary, see the next section.

    -   Attribute type: Property. [StructuredValue](https://schema.org/StructuredValue)
    -   Attribute metadata:
        -   `dateModified` : Last update timestamp of this attribute.
            -   Metadata type: [DateTime](https://schema.org/DateTime)
            -   Read-Only. Automatically generated.
    -   Mandatory

-   `name` : A mnemonic name given to the device.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        `https://uri.etsi.org/ngsi-ld/name` equivalent to [name](https://schema.org/name)
    -   Optional

-   `description` : Device's description.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        `https://uri.etsi.org/ngsi-ld/description` equivalent to [description](https://schema.org/description)
    -   Optional

-   `dateFirstUsed` : A timestamp which denotes when the device was first used.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional

-   `softwareVersion` : The software version of this device or URL to the release tag or DOI of algorithm software implementation.

    -   Attribute type: Property. [Text](https://schema.org/Text) or [URL](https://schema.org/URL)
    -   Optional

-   `provider` : The provider of the executed data quality checks implementation.

    -   Attribute Type: Property. [Provider](http://schema.org/provider)
    -   Normative References:
        [https://schema.org/provider](https://schema.org/provider)
    -   Optional

-   `refDeviceModel` : The device's model.

    -   Attribute type: Property. Reference to an entity of type
        [DeviceModel](../../DeviceModel/doc/spec.md).
    -   Optional

-   `deviceState` : State of this device from an operational point of view. Its
    value can be vendor dependent.

    -   Type: [Text](https://schema.org/Text)
    -   Attribute metadata:
        -   `timestamp`: Timestamp when the last update of the attribute
            happened. This value can also appear as a FIWARE
            [TimeInstant](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant)
            -   Type: [DateTime](http://schema.org/DateTime)
    -   Optional

-   `dateLastValueReported` : A timestamp which denotes the last time when the
    device successfully reported data to the cloud.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Mandatory

-   `dateModified` : Last update timestamp of this entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateCreated` : Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

## Configuration parameters

For each of the data quality checks and each of the measured parameters that need to be checked, a number of configuration settings are required and are stored in the `configuration` field.

- Minimum maximum bounds: Requires a `minimum` and `maximum` configuration value. Outside these boundaries, the measurements is defined unreliable.
- Jump: Requires a `jump_limit` configuration value. Changes in between two measurement points larger than this limit are defined unreliable.
- Stationary: Requires a `tolerance` and a `duration` configuration value. Measurements with a difference smaller than the given tolerance for the given duration of time are defined unreliable.
- Zscore: Requires a `zscore` configuration value. Measurements outside the boundaries based on the z-score are defined unreliable.

Each of the values are defined in the same unit as the data on which the quality checks are applied, unless the `unitCode` is provided explicitly.

## Test it with a real service

...

## Issues

-   Should we - instead of using the Device as base and overloading configuration field - not write a custom Device model and Device tailor made to quality checks?
