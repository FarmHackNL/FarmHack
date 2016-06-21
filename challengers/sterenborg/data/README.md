De bestanden in deze directory geven een overzicht van de verschillende types data. Op [https://data.farmhack.nl/challengers/sterenborg](https://data.farmhack.nl/challengers/sterenborg) vind je alle data.

# Documentatie

De satellietbeelden en NDVI kaarten gebruiken het coördinatenstelsel WGS 84 / UTM zone 31N (EPSG:32631). De drone NDVI kaart gebruikt he coördinatenstelsel WGS 84 / UTM zone 32N (EPSG:32632) De `geojson` bestanden gebruiken WGS84 (EPSG:4326) coördinatenstelsel.

## Percelen

In `percelen.geojson` vind je alle percelen Nanne en Gert. Elk perceel heeft een unieke ID nummer, een naam, oppervlakte, gewas, ras, voorgaand gewas en een locatie.

## Satellietbeelden

`sentinel2-2016-04-01_demo.tif` is een Sentinel-2 voorbeeldbestand afgesneden op de percelen. De Sentinel bands zijn als volgt ingedeeld:

- red: band #4
- green: band #3
- blue: band #2
- near-infrared: band #8

 `spot7-2016-04-01_demo.tif` is een Spot-7 voorbeeldbestand afgesneden op de percelen. De Spot bands zijn als volgt ingedeeld

 - red: band #3
 - green: band #2
 - blue: band #1
 - near-infrared: band #4

## Dronebeelden

`ebee-raw_demo.tif` bevat demo data van de eBee drone.

## NDVI kaarten

In `sentinel2-ndvi_demo.tif` vind je een NDVI kaart op basis van Sentinel-2 data.

![](https://raw.githubusercontent.com/FarmHackNL/FarmHack/master/challengers/sterenborg/data/images/ndvi.png)

`ebee-ndvi_demo.geojson` is een NDVI vector kaart (punten) op basis van de dronebeelden.

![](https://raw.githubusercontent.com/FarmHackNL/FarmHack/master/challengers/sterenborg/data/images/ebee-ndvi.png)

## Puddles by Jan Clement
 `risicolocaties_oppervlakkige_afspoeling.geojson` shows where puddles are likely to form on Jacob's plots. It is derived from a watershed analysis based on the Dutch height map and information about the soil. The white lines/areas in the image below indicate larger quantities of water (i.e. streams and puddles).

 ![](https://raw.githubusercontent.com/FarmHackNL/FarmHack/master/challengers/vandenborne/data/images/watershed.png)

 This dataset is contributed by [Jan Clement](https://twitter.com/geo_jan) and Harry Massop of [Alterra](https://www.wageningenur.nl/en/Expertise-Services/Research-Institutes/alterra.htm). See the dataset's [documentation](http://www.wageningenur.nl/nl/Publicatie-details.htm?publicationId=publication-way-343536353534) (Dutch) for more information.