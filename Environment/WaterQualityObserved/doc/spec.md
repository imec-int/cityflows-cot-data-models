# Water Quality

## Description

Water Quality data model for IoW is intended to represent water quality parameters 
at a certain water mass: surface water, sewer or groundwater.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json).

-   `id` : Unique identifier. It shall be a URN in the form
    `urn:ngsi-ld:WaterQualityObserved:<identifier>` where `<identifier>` shall be a
    unique ID integer value.

-   `type` : Entity type. It must be equal to `WaterQualityObserved`.

-   `dateModified` (NGSIv2): Last update timestamp of this entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateCreated` (NGSIv2): Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dataProvider` : Specifies the URL to information about the provider of this information.

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `dateObserved` : The date and time of this observation in ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval.
    -   Attribute type: Property. [DateTime](https://schema.org/DateTime) or an ISO8601
        interval represented as [Text](https://schema.org/Text).
    -   Optional

-   `dateLastCalibrated` :  The date and time of the last callibration in ISO8601 UTC format.
    -   Attribute type: Property. [DateTime](https://schema.org/DateTime) or an ISO8601
        interval represented as [Text](https://schema.org/Text).
    -   Optional

-   `refDevice` : Reference to the IoW Sensor Device.
    -   Attribute type: `Relationship`. Reference to an entity of type `Device`
    -   Mandatory

-   `location` : Location where measurements have been taken, represented by a GeoJSON Point.

    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    -   Optional


### Water quality parameters

-   `temperature` : Temperature.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:
        -   `timestamp`: Timestamp of the actual date at which the measured value was obtained by the sensor. It can be omitted if the observation time is the same as the one captured by the `dateObserved` attribute at entity level. The date and time are represented in ISO8601 UTC format or by an ISO8601 interval.
            -   Type: [DateTime](http://schema.org/DateTime)
            -   Optional
        -   `rawValue`: Raw value (cfr. ADC) obtained by the sensor before translation to the physical parameter.
            -   [Number](http://schema.org/Number)    
            -   Mandatory
        -   `unitCode` : The unit code (text) of measurement given using the
        [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, `CEL` represents celsius degrees (°C).
            -   Type: [Text](https://schema.org/Text)
            -   Optional
        -  `statusCode`: A status code on the raw sensor reading. For the status codes translation table, see the next section
            -   Type: [Number](https://schema.org/Number)
            -   Optional
    -   Default unit: Celsius Degrees.
    -   Optional

-   `conductivity` : Electrical Conductivity.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:
        -   `timestamp`: Timestamp of the actual date at which the measured value was obtained by the sensor. It can be omitted if the observation time is the same as the one captured by the `dateObserved` attribute at entity level. The date and time are represented in ISO8601 UTC format or by an ISO8601 interval.
            -   Type: [DateTime](http://schema.org/DateTime)
            -   Optional
        -   `rawValue`: Raw value (cfr. ADC) obtained by the sensor before translation to the physical parameter.
            -   [Number](http://schema.org/Number)    
            -   Mandatory
        -   `unitCode` : The unit code (text) of measurement given using the
        [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, `D10` represents Siemens per meter (S/m).
            -   Type: [Text](https://schema.org/Text)
            -   Optional
        -  `statusCode`: A status code on the raw sensor reading. For the status codes translation table, see the next section
            -   Type: [Number](https://schema.org/Number)
            -   Optional
        - `phase`: Error indication of conductivity
            -   [Number](http://schema.org/Number)    
            -   Optional
    -   Default unit: Siemens per meter (S/m).
    -   Optional

-   `conductance` : Specific Conductance.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:
        -   `timestamp`: Timestamp of the actual date at which the measured value was obtained by the sensor. It can be omitted if the observation time is the same as the one captured by the `dateObserved` attribute at entity level. The date and time are represented in ISO8601 UTC format or by an ISO8601 interval.
            -   Type: [DateTime](http://schema.org/DateTime)
            -   Optional
        -   `rawValue`: Raw value (cfr. ADC) obtained by the sensor before translation to the physical parameter.
            -   [Number](http://schema.org/Number)    
            -   Mandatory
        -   `unitCode` : The unit code (text) of measurement given using the
        [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, `D10` represents Siemens per meter (S/m).
            -   Type: [Text](https://schema.org/Text)
            -   Optional   
        -  `statusCode`: A status code on the raw sensor reading. For the status codes translation table, see the next section
            -   Type: [Number](https://schema.org/Number)
            -   Optional     
    -   Default unit: Siemens per meter at 25 ºC (S/m).
    -   Optional

-   `tds` : Total dissolved solids.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:
        -   `timestamp`: Timestamp of the actual date at which the measured value was obtained by the sensor. It can be omitted if the observation time is the same as the one captured by the `dateObserved` attribute at entity level. The date and time are represented in ISO8601 UTC format or by an ISO8601 interval.
            -   Type: [DateTime](http://schema.org/DateTime)
            -   Optional
        -   `rawValue`: Raw value (cfr. ADC) obtained by the sensor before translation to the physical parameter.
            -   [Number](http://schema.org/Number)    
            -   Mandatory
        -   `unitCode` : The unit code (text) of measurement given using the
        [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, `M1` represents milligrams per liter (mg/L).
            -   Type: [Text](https://schema.org/Text)
            -   Optional
        -  `statusCode`: A status code on the raw sensor reading. For the status codes translation table, see the next section
            -   Type: [Number](https://schema.org/Number)
            -   Optional
    -   Default unit: milligrams per liter (mg/L).
    -   Optional

-   `salinity` : Amount of salts dissolved in water.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:
        -   `timestamp`: Timestamp of the actual date at which the measured value was obtained by the sensor. It can be omitted if the observation time is the same as the one captured by the `dateObserved` attribute at entity level. The date and time are represented in ISO8601 UTC format or by an ISO8601 interval.
            -   Type: [DateTime](http://schema.org/DateTime)
            -   Optional
        -   `rawValue`: Raw value (cfr. ADC) obtained by the sensor before translation to the physical parameter.
            -   [Number](http://schema.org/Number)    
            -   Mandatory
        -   `unitCode` : The unit code (text) of measurement given using the
        [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, `NX` represents parts per thousand (ppt, ‰).
            -   Type: [Text](https://schema.org/Text)
            -   Optional
        -  `statusCode`: A status code on the raw sensor reading. For the status codes translation table, see the next section
            -   Type: [Number](https://schema.org/Number)
            -   Optional
    -   Default unit: Parts per thousand (ppt).
    -   Optional

-   `pH` : Acidity or basicity of an aqueous solution.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:
        -   `timestamp`: Timestamp of the actual date at which the measured value was obtained by the sensor. It can be omitted if the observation time is the same as the one captured by the `dateObserved` attribute at entity level. The date and time are represented in ISO8601 UTC format or by an ISO8601 interval.
            -   Type: [DateTime](http://schema.org/DateTime)
            -   Optional
        -   `rawValue`: Raw value (cfr. ADC) obtained by the sensor before translation to the physical parameter.
            -   [Number](http://schema.org/Number)    
            -   Mandatory
        -   `unitCode` : The unit code (text) of measurement given using the
        [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, `Q30` represents pH.
            -   Type: [Text](https://schema.org/Text)
            -   Optional
        -  `statusCode`: A status code on the raw sensor reading. For the status codes translation table, see the next section
            -   Type: [Number](https://schema.org/Number)
            -   Optional
    -   Default unit: Negative of the logarithm to base 10 of the activity of the hydrogen ion.
    -   Optional

-   `orp` : Oxidation-Reduction potential.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:
        -   `timestamp`: Timestamp of the actual date at which the measured value was obtained by the sensor. It can be omitted if the observation time is the same as the one captured by the `dateObserved` attribute at entity level. The date and time are represented in ISO8601 UTC format or by an ISO8601 interval.
            -   Type: [DateTime](http://schema.org/DateTime)
            -   Optional
        -   `rawValue`: Raw value (cfr. ADC) obtained by the sensor before translation to the physical parameter.
            -   [Number](http://schema.org/Number)    
            -   Mandatory
        -   `unitCode` : The unit code (text) of measurement given using the
        [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, `2Z` represents millivolts (mV).
            -   Type: [Text](https://schema.org/Text)
            -   Optional
        -  `statusCode`: A status code on the raw sensor reading. For the status codes translation table, see the next section
            -   Type: [Number](https://schema.org/Number)
            -   Optional
    -   Default unit: millivolts (mV).
    -   Optional
    
### Status code table

The following table clarifies the possible `statusCode` as provided by the sensor:

| STATUS      |  STATUS CODE          |     
|---------|-----------|
|    AFE_INIT_ERROR                         |      =0x3C |
|    GPIO_INTER_INIT_ERROR                  |     =0x40 |
|    GPIO_INRTRRUPT_SOURCE_ERROR            |     =0x41 |
|    GPIO_WAKE_UP_INTERRUPT_ERROR           |     =0x42 |
|    WTU_INIT_ERROR                         |     =0x50,   |
|    WTU_CLOCK_INIT_ERROR                   |     =0x51 |
|    WTU_CLOCK_COMPARATOR_ERROR             |     =0x54 |
|    WTU_CLOCK_SOURCE_ERROR                 |     =0x55 |
|    WTU_CLOCK_SET_INTERVAL_ERROR           |     =0x56 |
|    WTU_CLOCK_SET_INTERUPT_ERROR           |     =0x57 |
|    WTU_CLOCK_SET_WAKUEUP_ERROR            |     =0x58 |
|    WTU_CLOCK_SET_PRESCALER_ERROR          |     =0x59 |
|    WTU_CLOCK_SET_PERIODIC_ERROR           |     =0x5A |
|    WTU_CLOCK_SET_ENABLE_ERROR             |     =0x5B |
|    WTU_WAKE_UP_ERROR                      |     =0x5C |
|    GPT_INIT_ERROR                         |    =0x60 |
|    GPT_CONFIG_ERROR                       |    =0x61 |
|    GPT0_CONFIG_ERROR                      |    =0x62 |
|    GPT1_WAITING_TIME_ERROR                |    =0x63 |
|    GPT_UNINIT_ERROR                       |    =0x64 |
|    WDT_INIT_ERROR                         |     =0x68 |
|    WDT_RESET_ERROR                        |     =0x69 |
|     STRING_PAERING_ERROR                  |     =0x70 |
|     STRING_TOO_LONG_COMMANDCHAIN_ERROR    |     =0x71 |
|     STRING_SINGLE_COMMAND_LENGHT_ERROR    |     =0x72 |
|     STRING_CHECK_SUME_ERROR               |     =0x73 |
|     COMPUTING_FREQUENCY_ERROR             |     =0x85 |
|     EXTERNAL_INTERUPT_ERROR               |     =0x86 |
|    CENTRAL_STABLE_CURRENT_ERROR           |    =0x87 |
|     COMPUTING_IMPEDANCE_ERROR             |     =0x88 |
|     DC_ADC_RUN_ERROR                      |     =0x90 |
|     DC_RUN_ERROR                          |     =0x91 |
|     FEE_WRITE_ERROR                       |     =0xA0 |


## Use it with a real service

...

## Open Issues

- Do we need `rawValueUnitCode` as well?
- Should bitcodes be used which can be or'ed together (see issue 15 to have a single statusCode in the datamodel ? 

## Remarks

- metadata fields is not covered in the key-value version of the data (and json-schema validation). So, for application that require the metadata, we need to use the normalized version.
