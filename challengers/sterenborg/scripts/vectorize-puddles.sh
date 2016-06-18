#!/usr/bin/env bash

gdalwarp -q -cutline percelen-RD.shp -crop_to_cutline -of GTiff aandeel_natte_plekken.tif anp_clipped.tif

gdal_calc.py -A anp_clipped.tif --outfile=puddles.tif --calc="A==25" --NoDataValue=0

gdal_polygonize.py puddles.tif puddles.shp