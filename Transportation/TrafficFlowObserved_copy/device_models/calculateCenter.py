import time
import re
import json
import requests
from pyproj import transform, Proj

def calculate_grid(binId):
    """ calculates the size of a proximus grid, based on the id of the bin

    input: binId
    formula: the first digits countain the square size in meters of the bin,
    the next text has the Lambert coordinates (divided by 100) of the bottom-left corner.
    The whole square of coordinates is calculated and the coordinates, in WGS-84
    GPS coordinates, is returned.
    output: dict with 'grid' item containing list of coordinates tuples, 'center' item for the center of thie square
    """

    matches = re.match('([0-9]+)m[E,W]([0-9]+)[N,S]([0-9]+)', binId)
    offset = int(matches.group(1))
    x = int(matches.group(2))
    y = int(matches.group(3))

    multiplicator = 100 #needed to get the right units
    coordinates_lambert = [[x*multiplicator, y*multiplicator], [x*multiplicator + offset, y*multiplicator],
        [x*multiplicator + offset, y*multiplicator + offset], [x*multiplicator, y*multiplicator + offset]]
    center_point_lambert = [x*multiplicator + offset / 2, y*multiplicator + offset / 2]
    center_point_wgs_84 = coordinate_lambert_to_WGS84(center_point_lambert[0], center_point_lambert[1])
    #coordinaten omzetten naar GPS
    coordinates_wgs_84 = [coordinate_lambert_to_WGS84(coordinates_lambert[0][0], coordinates_lambert[0][1]), 
                         coordinate_lambert_to_WGS84(coordinates_lambert[1][0], coordinates_lambert[1][1]), 
                         coordinate_lambert_to_WGS84(coordinates_lambert[2][0], coordinates_lambert[2][1]), 
                         coordinate_lambert_to_WGS84(coordinates_lambert[3][0], coordinates_lambert[3][1])]
    return {'grid': coordinates_wgs_84, 'center': center_point_wgs_84}

def coordinate_lambert_to_WGS84(x,y):
    """ returns an dict of lon,lat coordinates

    input: coordinaten in CRS = EPSG 3035
    towards EPSG WGS 84 standaard GPS coordinaten (EPSG 4326)
    the transformation will be done using the pyProj package.
    (https://pyproj4.github.io/pyproj/dev/api/transformer.html#pyproj-transform) 
    If this fails, another try is done through an API:
    https://github.com/klokantech/epsg.io
    """

    #using pyProj package to avoid dependence on API module
    pIn = Proj(init='EPSG:3035')
    pOut = Proj(init='EPSG:4326')
    try: 
        new_x, new_y = transform(pIn,pOut, x, y)
        return {'lon': round(new_x,8), 'lat': round(new_y,8)}
    except:
        #using API if pyProj fails
        api_token = 'your_api_token'
        api_url_base = 'http://epsg.io/trans'
        api_url = api_url_base
        headers = ''
        variable={'x': str(x), 'y': str(y), 'z' : '0',
                's_srs' : 3035, 't_srs' : 4326, 'callback':'jsonpFunction'}    
        response = requests.get(api_url, headers=headers, params=variable)

        if response.status_code == 200:
            # print(json.loads(response.content.decode('utf-8')[14:-1]))
            temp = json.loads(response.content.decode('utf-8')[14:-1])
            return {'lon': float(temp['x']), 'lat': float(temp['y'])}

        return None