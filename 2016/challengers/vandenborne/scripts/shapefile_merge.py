#!/usr/bin/python

# Merges a directory of disparate Shapefiles into a single Shapefile
# source: http://geospatialpython.com/2013/04/add-field-to-existing-shapefile.html

import shapefile
import os
import subprocess

path = './'

for f in os.listdir(path):
    if '.shp' in f:
        source = shapefile.Reader(f)
        destination = shapefile.Writer()
        destination.fields = list(source.fields)

        destination.field('perceel', 'C', '100')

        for record in source.records():
            record.append(f.split('.')[0])
            destination.records.append(record)

        print destination.records

        destination._shapes.extend(source.shapes())
        destination.save('./merged/%s' % f)

        destination = None
        source = None

# merge all files into one shapefile
subprocess.call('cd merged; for f in *.shp; do ogr2ogr -update -append merged.shp "$f" -f "ESRI Shapefile"; done;', shell=True)

# create geojson file
# Warning: this can become quite big
# subprocess.call('cd merged; ogr2ogr -f GeoJSON merged.geojson -s_srs EPSG:4326 -t_srs EPSG:4326 merged.shp;', shell=True)

#remove unneeded Shapefiles
subprocess.call("cd merged; find . -type f ! -name 'merged.*' -delete", shell=True)
