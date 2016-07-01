from __future__ import division
from shapely.wkt import loads
from shapely.geometry import mapping
import urllib, json
import sys

# load the api key
try:
    apikey = str(sys.argv[1])
except:
    apikey = ''


# construct the first url
base_url = "https://www.crop-r.com"
api_url = "/api/v1/cropfield/?format=json&sessionid="+apikey
response_list = []

# download until all features are loaded
while api_url != None:
    url = base_url+api_url
    response = urllib.urlopen(url)
    data = json.load(response)
    response_list += [data] # store the json into a list
    api_url = data['meta']['next'] # check for the next url

# open crop names json
with open('../../crop-r_lookup.json') as crop_file:
    crop_data = json.load(crop_file)

def return_crop_name(crop_data,number):
    crop_name = None
    if number == None:
        number = 0
    else:
        number = int(number)
    for item in crop_data['croptype_list']:
        if item['id'] == number:
            crop_name = item['name']
    return crop_name

# construction of the geojson file
out = {'type': 'FeatureCollection', 'features': []}
for response in response_list:
    for cropfield in response['objects']:
        id = cropfield['id']
        year = cropfield['period_start'].split("-")[0]
        name = cropfield['name']
        crop = cropfield['crop']
        crop_name = return_crop_name(crop_data,crop)
        farm = cropfield['farm']
        previous_crop = cropfield['previous_crop']
        previous_crop_name = return_crop_name(crop_data,previous_crop)
        geom = loads(cropfield['geometry'])
        out['features'].append({'properties': {
            'id': id,
            'year': year,
            'name': name,
            'crop': crop,
            'crop_name': crop_name,
            'farm': farm,
            'previous_crop': previous_crop,
            'previous_crop_name': previous_crop_name
        },
        'type': 'Feature', 'geometry': mapping(geom)})

# write to geojson
with open('./tmp/data.geojson', 'w') as outfile:
    json.dump(out, outfile)

