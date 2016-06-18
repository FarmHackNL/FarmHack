De bestanden in deze directory geven een overzicht van de verschillende types data. Op [https://data.farmhack.nl/challengers/vandenborne](https://data.farmhack.nl/challengers/sterenborg) vind je alle data.

# Documentatie

## Percelen

In `percelen.geojson` vind je alle percelen Nanne en Gert. Elk perceel heeft een unieke ID nummer, een naam, oppervlakte, gewas, ras, voorgaand gewas en een locatie.

## Satellietbeelden

`sentinel2-2016-04-01_demo.tif` is een Sentinel-2 voorbeeldbestand afgesneden op de percelen.

 `spot7-2016-04-01_demo.tif` is een Spot-7 voorbeeldbestand afgesneden op de percelen.

## Dronebeelden

`ebee-raw_demo.tif` bevat demo data van de eBee drone.

## NDVI kaarten

In `sentinel2-ndvi_demo.tif` vind je een NDVI kaart op basis van Sentinel-2 data.

![](https://raw.githubusercontent.com/FarmHackNL/FarmHack/master/challengers/sterenborg/data/images/ndvi.png)

`ebee-ndvi_demo.geojson` is een NDVI vector kaart (punten) op basis van de dronebeelden.

![](https://raw.githubusercontent.com/FarmHackNL/FarmHack/master/challengers/sterenborg/data/images/ebee-ndvi.png)

De rasterbestnanden gebruiken het Nederlandse coördinatenstelsel (RD/EPSG:28992). De `geojson` bestanden gebruiken lat/lon (WGS84/EPSG:4326).