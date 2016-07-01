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


# download files
base_url = "https://www.crop-r.com"
api_url = "/api/v1/cropfield/?format=json&sessionid="+apikey
response_list = []

##

while api_url != None:
    url = base_url+api_url
    response = urllib.urlopen(url)
    data = json.load(response)
    response_list += [data]
    api_url = data['meta']['next']

# response contains the returned JSON object
out = {'type': 'FeatureCollection', 'features': []}
for response in response_list:
    for cropfield in response['objects']:
        id = cropfield['id']
        geom = loads(cropfield['geometry'])
        out['features'].append({'properties': {'id': id}, 'type': 'Feature', 'geometry': mapping(geom)})

# write to geojson
with open('./tmp/data.geojson', 'w') as outfile:
    json.dump(out, outfile)

