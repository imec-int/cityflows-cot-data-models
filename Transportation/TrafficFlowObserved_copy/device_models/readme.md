# Device models for cityflows

The device models are currently all virtual sensors. Incoming data can be linked to these virtual data providers. 

## Naming conventions

Naming conventions are described [here](https://iminds.atlassian.net/wiki/spaces/TES/pages/1619132691/Generic+NGSI+-LD+entity+ID+structure).

## Proximus
Proximus data gives a snapshot of the amount of people in a geograhical box. The binId of the dataStream encodes the location and area of this box, thus encoding information about this virtual sensor. As such, there is a 1-1 relationship between binId's and proximus virtual devices. Given the binId, the center of this box can be calculated and will be used as the location of the particular device. 
The proximus device model is described [here](proximus_cellular_data.json), device models can be found [here](devices_proximus_cellular/).

If a data stream is fed, it should be checked if the device already exists. If not, a new device must be created, using [this script](calculateCenter.py) to determine the location of the virtual sensor based on the binId.

## Citymesh
Citymesh data gives a count of the unique visitors of an area surrounding a wifi scanning device between two timestamps. Every wifi scanner corresponds to a virtual measuring device. In the smart zone of Antwerp, we currently have 6 wifiscanners active. Given the location of the wifi scanner, a polygon of radius 75 meters around this device is created to gauge the range of the wifi scanner. 
The Citymesh device model is described [here](citymesh_device_model.json), device models can be found [here](devices_citymesh/).

## Telraam
Telraam devices are abstracted by the street segment they are counting on. We identify a Telraam by its Road Registry OIDN (link). These devices count pedestrian, bike, car and lorry traffic when there is enough daylight for the sensors to do so.
The Telraam stream should be split into 4 different entities, one for each modality (pedestrian, bike, car, lorry). This is important to ensure that for each of these modalities, always the latest registred value is available.
The Telraam device model is described [here](telraam_data.json), device models can be found [here](devices_citymesh/).