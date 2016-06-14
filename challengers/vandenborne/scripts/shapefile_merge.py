'''Merges a directory of sseparate Shapefiles into a single Shapefile'''

import shapefile
import os
import subprocess

path = './'

for file in os.listdir(path):
    if '.shp' in file:
        source = shapefile.Reader(file)
        destination = shapefile.Writer()
        destination.fields = list(source.fields)

        for field in destination.fields:
            if 'perceel' not in field[0]:
                destination.field('perceel', 'C', '100')

            for record in source.records():
                record.append(file.split('.')[0])
                destination.records.append(record)

            destination._shapes.extend(source.shapes())
        destination.save('./merged/%s' % file)

# merge all files into one shapefile
# subprocess.call('cd merged; for f in *.shp; do ogr2ogr -update -append merged.shp "$f" -f "ESRI Shapefile"; done;')