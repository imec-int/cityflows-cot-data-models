# Data conversie Imec IoW sensors

## Octa payload

The Octa boards send a byte stream with all information about a particular measurement. Details of this protocol are outside of scope of this document. Those protocol details are described in a separate document, for a broader public than just this project. I will send a copy around, but note that this is not authorative: the latest version should be requested from the Octa developers.

Within the Octa protocol, all values are preceded by a `message type` to indicate what the value is for. The following Octa payload `message types` are used:

| Type | Short name      | Description |
|------|-----------------|-------------|
|  4   | box_temperature | The temperature (in Kelvin) within the WQMD box. Note: not the water temperature! |
|  5   | box_humidity    | The humidity within the WQMD box (in %) |
| 20   | counter         | Message counter, also used to calculate time of measurement |
| 24   | battery         | Battery voltage (in mV) |
| 25   | octa_state      | Octa status code |
| 26   | sensor_id       | The sensor ID |
| 27   | impedance       | Impedance (in Ohm) |
| 28   | phase           | Phase |
| 29   | sensor_state    | Sensor status code |
| 30   | pH              | (Micro)voltage for pH measurement |
| 33   | temperature     | Temperature (in decidegrees celsius) |
| 36   | octa_id         | The ID of the Octa board |

From now on, these fields will be referenced by their short name, prefixed with `I:`. For example, the temperature from the Octa payload is `I:temperature`

## Sensor calibration parameters

The following calibration parameters should be set on the sensor device entity in the context broker. Please not the distinction between sensor and measuring box entities! These parameters should be fetched by any script doing ingress. The `I:sensor` from the Octa input byte stream should be used to identify which sensor to fetch.

 * conductivity.k_cell
 * pH.gain
 * pH.offset
 * temperature.offset
 * battery.gain
 * battery.offset

These fields will be referenced by their name as described above, prefixed with `CP:`. For example, the temperature offset is `CP:temperature.offset`

## Device <-> entity mapping

Device mapping by the CoT platform should be done by using:

primary device alternative ID: [I:sensor_id]
parent device alternative ID: [I:octa_id]

For clarity, the NGSI ID of the parent device (the Octa) is being referenced in the `refParentDevice` field of the primary device (the sensor). By providing both alternative IDs, this reference can/should be automatically updated.

## Transformation

This section describes the formulas used to translate the raw input into the values stored in the context broker.

### Conductivity

```
conductivity.value = 1,000,000 * [CP:conductivity.k_cell] / [I:impedance]
conductivity.metadata.unitCode = "G42"
conductivity.metadata.rawValue = [I:impedance]
conductivity.metadata.rawValueUnitCode = "OHM"
conductivity.metadata.phase = [I:phase]
```

### pH

```
pH.value = ( ( [I:pH] / 1000 ) - [CP:pH.offset] ) / [CP.pH.gain]
pH.metadata.unitCode = "Q30"
pH.metadata.rawValue = [I:pH]
pH.metadata.rawValueUnitCode = "D82"
```

### Temperature

```
temperature.value = ( [I:temperature] / 10 ) + [CP:temperature.offset]
temperature.metadata.unitCode = "CEL"
temperature.metadata.rawValue = [I:temperature] / 10
temperature.metadata.rawValueUnitCode = "CEL"
```

### Battery level

Battery level needs to be included both in the parent `Device` entity as in the `WaterQualityObserved` entity.

For the `WaterQualityObserved` entity:

```
batteryLevel.value = ( [I:battery] - [CP:battery.offset] ) / [CP:battery.gain]
batteryLevel.metadata.rawValue = [I:battery]
batteryLevel.metadata.rawValueUnitCode = "2Z"
```

For the `Device` entity:

```
batteryLevel.value = ( [I:battery] - [CP:battery.offset] ) / [CP:battery.gain]
```

### Device humidity

```
deviceHumidity.value = [I:box_humidity]
deviceHumidity.metadata.unitCode = "P1"
```

### Device temperature

```
deviceTemperature.value = [I:box_temperature]
deviceTemperature.metadata.unitCode = "CEL"
```

### Status codes

For the `WaterQualityObserved` entity:

```
reliability.value = 1
reliability.metadata.octa_state = [I:octa_state]
reliability.metadata.sensor_state = [I:sensor_state]
octa_state.value = [I:octa_state]
sensor_state.value = [I:sensor_state]
```

Note that both the Octa status code as the sensor status code is stored redundantly. This is done for forward compatability. I feel that these status codes should be in the metadata of the reliability attribute. However, for now, metadata is not yet stored in the time series database. Therefore, separate attributes are required.

However, if [I:octa_state] > 15 or [I:sensor_state] > 0, then there is an error. This means that the `reliability.value` should be set to 0 instead. Furthermore, the `Device` entity is not healthy:

```
healthState.value = "faulty"
```

The `healthState` should otherwise be determined by the IoT agent, based on the regular metrics (ie. be set to 'down' if the interval was too long).
