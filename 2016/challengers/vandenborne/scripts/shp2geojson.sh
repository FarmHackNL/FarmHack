#!/usr/bin/env bash

#source: ... lost it :(

NEWDIR=${2:-"./geojson/"}
for FILE in ${1:-}*.shp # cycles through all files in directory (case-sensitive!)
do
    SIZE=$(ls -al "$FILE" | awk '{print $5}')
    echo "$SIZE bytes"
    if [ "$SIZE" -gt "30000000" ]
    then
        echo "WARNING: Skipping $FILE because it's pretty big and GitHub might complain!"
        continue
    fi
    FILENEW=`echo | basename "$FILE" | sed "s/.shp/.geojson/"` # replaces old filename
    echo "converting file: $FILE into $FILENEW..."
    ogr2ogr \
    -f 'GeoJSON' \
    -s_srs 'EPSG:4326' \
    -t_srs 'EPSG:4326' \
    "$NEWDIR$FILENEW" "$FILE"
done
exit
