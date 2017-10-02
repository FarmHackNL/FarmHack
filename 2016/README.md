# FarmHack

[![Join the chat at https://gitter.im/FarmHackNL/FarmHack](https://badges.gitter.im/FarmHackNL/FarmHack.svg)](https://gitter.im/FarmHackNL/FarmHack?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

_FarmhackNL mobiliseert coders, creatieven en domeinexperts op vraagstukken van de boer._

Tijdens 4 (!) hackathons in juni en juli komen we samen bij de boer(!) om te hacken aan agri data, visualisaties, analyses en apps. Schrijf je snel in op [farmhack.nl](http://www.farmhack.nl)!


# Meedoen

Op [farmhack.nl](http://www.farmhack.nl) kun je je inschrijven voor één van de FarmHacks.

 Via de volgende kanalen kun je meediscussiëren en/of up-to-date blijven.

- [Blog](http://www.farmhack.nl/category/blog/) - laatste nieuws, interviews en blogs over data en tools.
- [Twitter](https://twitter.com/farmhacknl) - laatste nieuws, aankondigingen en live verslag van elke FarmHack.
- [Gitter](https://gitter.im/FarmHackNL/FarmHack) - openbaar chat kanaal.
- [Issue tracker](https://github.com/FarmHackNL/FarmHack/issues) - vraag/opmerkinge/suggestie voor FarmHack? Laat het ons weten!

Op https://github.com/FarmHackNL vind je een overzicht van de FarmHack projecten.

# Data

- In deze repository vind je (demo) datasets van de FarmHack Challengers, zie de `challengers/<challenger>/data` mapjes.
- In de FarmHack [Open Data](https://github.com/farmhacknl/open-data) repository verzamelen we (landelijke) **open** agri data die interessant/relevant is voor de FarmHacks.
- Op [data.farmhack.nl](https://farmhack.data.nl) vind je bulk downloads van (landelijke) open data en de data van de challengers.

# Documentatie en tools

In de [PDOK/NGR documentatie](http://pdok-ngr.readthedocs.io) vind je handleidingen en tutorials over het gebruik van geodata.

Het gros van de FarmHack  datasets heeft een ruimtelijk component. Gebruik een van onderstaande (web) apps om geodata te visualiseren, analyseren en transformeren naar andere bestandsformats.

- [CartoDB](https://cartodb.com) - Geodata in de browser
- [QGIS](http://www.qgis.org/en/site/) - Geodata op de desktop
- [PostGIS](http://postgis.net) - Geodata plug-in voor PostgresSQL
- [Turf.js](http://turfjs.org) - Geodata in JavaScript (browser én desktop)
- [GDAL](http://www.gdal.org) - Geodata in de terminal

**Vooral QGIS is een must have: hiermee kun je o.a. geodata slicen en naar andere bestandsformats tranformeren bijv. van Shapefile naar GeoJSON.**

# Challengers

**Jacob van den Borne - Reusel**

Verslag: [blog](http://www.farmhack.nl/resultaten-farmhack-1-datavisualisatie-pieperboer/) | [video](https://vimeo.com/171559771)

Demodata en documentatie: https://github.com/FarmHackNL/FarmHack/tree/master/challengers/vandenborne/data

Alle data: https://data.farmhack.nl/challengers/vandenborne/

**Nanne Sterenborg - Groningen**

Demodata en documentatie: https://github.com/FarmHackNL/FarmHack/tree/master/challengers/sterenborg/data

Alle data: https://data.farmhack.nl/challengers/sterenborg/

**Ilona Lagas en Jos van Leussen - Zwolle**

Ilona Lagas is de voorzitter van Vechtdalproducten, een coöperatie in het Overijssels Vechtdal waarin producenten (boeren), bewerkers (bakkers en slagers) en gebruikers in de horeca (restaurants en hotels) zijn verenigd.

Jos van Leussen is de initiatiefnemer van ‘De Zwolse Stadslanderijen’, een boerenbeheer maatschappij die zich richt op het beheer en gebruik van een deel van de ‘reservegronden woningbouw’: honderden hectaren grond in en rond de stad die ooit bedoeld waren voor woningbouw.

**Nienke Dirx-Kuijken - Noord-Brabant**

Ninke Dirx-Kuijken is innovatiemanager bij [Varkens Innovatie Centrum Sterksel](http://www.wageningenur.nl/nl/Expertises-Dienstverlening/Onderzoeksinstituten/livestock-research/Innovatiecentra-en-faciliteiten/Varkens-Innovatie-Centrum-Sterksel.htm), een multifunctioneel onderzoekscentrum voor innovatieve en duurzame varkenshouderij.

 Al een aantal jaar kijkt zij naar de kansen van digitalisering. Resultaten laten zien dat veel winst te behalen valt met data gedreven management. Vooral als straks de slag gemaakt wordt van meten op groepsniveau naar individueel dierniveau.

# Data donoren

|Donor(en)|Organisatie/Bedrijf|Dataset|Challenger(s)|
|---|---|---|---|
|Ton van Gastel|[Eurofins Agro](http://www.blgg.com)|[Bodemscout](http://www.mijnpercelen.nl?returnUrl=%2FKaartbedrijf)| Van den Borne, Sterenborg|
|[Jan Clement](https://twitter.com/geo_jan), Harry Massop|[Alterra](https://www.wageningenur.nl/en/Expertise-Services/Research-Institutes/alterra.htm)|[Potentiële risicolocaties voor oppervlakkige afspoeling](http://www.wageningenur.nl/nl/Publicatie-details.htm?publicationId=publication-way-343536353534)| Van den Borne, Sterenborg|

# De FarmHack visie

FarmHack is een katalysator voor oplossingen en innovaties in de agrarische en landbouwsector. We mobiliseren coders, creatieven en domeinexperts op vraagstukken van de boer. De ambitie is om uit te groeien tot een permanent vernieuwingskracht binnen de agri- en landbouwsector: een gemeenschap die uitdagingen op een open en transparante manier aanpakt. Het motto hierbij is: make things open: it makes things better.

Om dit te realiseren willen alle analyses, visualisaties, apps, en de bijbehorende ontwikkelproces en data die tijdens de FarmHacks aan bod komen op een open en duurzame manier vastleggen. Het streven: een solide gemeenschappelijke basis realiseren waarop we rendabele apps en oplossingen kunnen bouwen. Een gezamenlijke verkenning van de agri/landbouw _problem space_ stelt ons beter in staat om waarde toevoegende apps en oplossingen te bouwen. Samen kunnen we tijdrovende bottlenecks effectiever wegnemen. Want, wat is waardevoller en fijner: een uur lang obscure data schoonmaken of je toffe app productieklaar en gepolijst maken?

**We richten FarmHack daarom in als een open source project: we ontwikkelen en communiceren in het open.** Maak daarom veelvuldig gebruik van de FarmHack ecosysteem op GitHub.
