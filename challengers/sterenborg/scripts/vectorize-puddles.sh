#!/usr/bin/env bash

# Extract the puddles from Jan Clement's watershed analyses and convert them to a vector file

gdalwarp -q -cutline percelen-RD.shp -crop_to_cutline -of GTiff aandeel_natte_plekken.tif anp_clipped.tif

gdal_calc.py -A anp_clipped.tif --outfile=puddles.tif --calc="A==25" --NoDataValue=0

gdal_polygonize.py puddles.tif puddles.shp
