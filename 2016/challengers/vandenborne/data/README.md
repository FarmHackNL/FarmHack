De bestanden in deze directory geven een overzicht van de verschillende types data. Op [https://data.farmhack.nl/challengers/vandenborne](https://data.farmhack.nl/challengers/vandenborne) vind je alle data.

# Documentatie

Onderstaande komt uit Frenk-Jan Barons BSc thesis `Bodemscans en opbrengstmeting in de aardappelteelt op zandgrond: het zoeken naar verbanden`.

## 1. Percelen

Jacobs percelen zijn over een groot gebied verspreid (sommige liggen in Belgie!). Ze komen in alle soorten, maten en vormen voor. Elk perceel heeft een unieke ID nummer, een naam, oppervlakte, gewas, ras, voorgaand gewas en een locatie.

## 2. Bodemscan

Een bodemscan meet de elektrische geleidbaarheid en magnetische gevoeligheid van de bodem. Bodemscans geven inzicht in de samenstelling van de bodem en de locaties van droge en natte plekken. Aan de hand hiervan kan de vruchtbaarheid bepaald worden. De bodemscan bestanden hebben één kolom: `EC`. Dit staat voor _electrical conductivity_ en is een maat voor de vruchtbaarheid van het perceel.

Lees meer over de bodemscans op http://www.vandenborneaardappelen.com/nl/361/bodemscannen-bij-van-den-borne-aardappelen

## 3. Schaduwkaarten

Van elk perceel worden er schaduwkaarten gemaakt. Deze geven het schaduwverloop van een perceel aan de hand van een aantal categorieen: permanente schaduw, transitieschaduw, etc. Jacob gebruikt deze gegevens om o.a. de gewasdichtheid te bepalen: planten in de schaduw worden verder van elkaar geplant dan planten in de open lucht. 

Lees meer over variabel poten op http://www.vandenborneaardappelen.com/nl/363/variabel-poen-in-schaduwzones

## 4. Pootlogs

De zaai- en -pootlogs laten zien hoe machines naar percelen rijden en wat ze daar zaaien. Elk perceel wordt nauwkeurig ingemeten alvorens het gezaaid wordt met een gewas.

Het poten gebeurt variabel, de pootafstand is dus niet overal gelijk. Er zijn drie manieren waarop variabel gepoot wordt:

1. In de spuitsporen, de planten in de spuitsporen krijgen meer licht omdat er minder concurrentie is dus wordt er dichter op elkaar gepoot.
2. In de schaduwzones, de planten in de schaduw krijgen minder licht en zullen daarom achterblijven in de groei, om toch een uniforme maatsortering te krijgen worden de planten hier verder uit elkaar gepoot.
3. Op basis van bodemgeleidbaarheid, op plaatsen met een hogere geleidbaarheid wordt dichter op elkaar geplant omdat de bodem daar een hogere opbrengstpotentie heeft. Er is namelijk meer vocht beschikbaar.

Ook kan er tijdens het poten variabel vloeibare kunstmest toegediend worden en/of granulaat gestrooid worden. Deze gegevens worden allemaal opgeslagen in de .csv files. Hierin staan eerst weer de algemene gegevens en daarna
- de course: het pad dat de machine volgt, de hoek ten opzichte van het noorden.
- fix is de kwaliteit van het Gps signaal.
- row is het nummer van de rij die gepoot wordt, er worden namelijk vier rijen gepoot. In de spuitsporen worden rij één en vier uitgezet. Elke drie meter wordt er een meting gedaan,
- onder # staan het aantal knollen dat in die drie meter geplant is. Hiermee wordt de huidige plantafstand berekend en kan deze vergeleken worden met de ingestelde waarde.

Hierna volgt hoeveel granulaat en vloeibare kunstmest ingesteld is en hoeveel daadwerkelijk gegeven wordt. Verder staan er nog de naam van de bestuurder, het ras, de maat van het pootgoed en welke soort vloeibare kunstmest is toegepast.

Lees meer over het variabel poten op http://www.vandenborneaardappelen.com/nl/292/variabel-poten

## 6. Gewassensing

De Fritzmeier Isaria sensor meet de reflectie van het licht dat op een plant valt. Hieruit zijn o.a. de hoeveelheid biomassa en stikstof van een plant te bepalen. Elk meting is voorzien van een nauwkeurige GPS coordinaat. De metingen worden gebruikt om taakkaarten te maken voor het variabel toedienen van mest en/of kunstmest. Het gewas krijgt op deze manier precies wat het nodig heeft en wordt verspilling tegengegaan.

De sensor meet twee waardes:

- IRMI: is een waarde voor de Red-Edge Position (REP). Deze index geeft aan hoeveel stikstof er in de plant aanwezig is. Aan de hand van deze data kan bepaald worden hoeveel stikstof er nog bijgestrooid moet worden. Hiervoor worden er taakkaarten van de data gemaakt of wordt er meteen na de meting variabel vaste of vloeibare kunstmest toegediend.
- IBI: een biomassa index. Deze index geeft weer hoe groen het oppervlakte is, de waarde kan variëren tussen 0 en 1. Als de grond kaal is geeft de sensor 0 en 1 staat voor een sterk en goed groeiend gewas dat heel de grond bedekt heeft.

In het bestand vind je verder de kolommen 

- sprayer: geeft % aan van de ingestelde spuitvloeistof (meestal 100%)
- section: staat voor welke sectie deze procenten gelden.

Aan de hand van de metingen kan de machine meteen variabel kunstmest strooien. Als er MAP (Mapping) in de naam van de file staat is er alleen gemeten; als er POT (Potato) in de naam van de file staat is er gespoten.

Lees meer over gewassensing op http://www.vandenborneaardappelen.com/nl/296/gewassensing

## 7. Opbrengstmeting

Beide aardappelrooiers (de Puma 3 en de Puma+) zijn uitgerust met een opbrengstmetingsysteem.

De ruwe data in .csv files is als volgt opgebouwd: datum, tijd, positie, kwaliteit gps signaal, aantal satellieten, x en y in meters.

De volgende kolom is de snelheid van de rooier in km/h, daarna komt het gewicht van de aardappels op het bunkerbandje. Hier moet alleen nog wel het leeggewicht van het bandje afgetrokken worden, dat staat in de volgende kolom. Met de conversie factor wordt gecorrigeerd voor de tijd dat de aardappels onderweg zijn in de machine. Daarna volgen de snelheid van het bunkerbandje in meter per seconde en de werkbreedte van de machine. Dit is drie meter omdat er vier rijen van 75 centimeter gerooid worden.

Nu komen de opbrengsten waar het om gaat,
 - yield (ton/ha): de opbrengst in ton per hectare voor elke positie
 - totalyield (ton/ha): de totale opbrengst in tonnen, dit is de som van alle voorgaande puntmetingen
 - totalarea(ha): het aantal gerooide hectares

In sommige bestanden zijn ook gegevens uit de boordcomputer van de rooier opgenomen. Dit zijn het aantal motortoeren (rpm) , benodigd koppel, geleverd koppel, brandstofverbruik in liter per uur, totaal brandstofverbruik in liters. De tractrear is de olie druk van de wielaandrijving van de rooier. Als de grond verdicht is zal het rooien zwaarder gaan en is er meer olie druk nodig, deze parameter kan dus een indicator zijn voor de bodemverdichting.

Lees meer over de opbrengstmeting op http://www.vandenborneaardappelen.com/nl/300/opbrengstmeting

## Bodemscan by Eurofins

Bodemscout shows a farmer where in his plots are spots where crops (almost) always grow better (blue) and where they (almost) always grow worse (red) then the average of the cropfield. 

The dataset has 7 possible values (1-7) and is symbolised like this

![](https://raw.githubusercontent.com/FarmHackNL/FarmHack/master/2016/challengers/vandenborne/data/images/bodemscan_eurofins_legend.gif)

- Value 1 means this rasterpoint has been always much worse then average for the field over 9 past years.
- Value 7 means this rasterpoint has been always much better then average for the field over 9 past years.
- Value 4 means this rasterpoint has always scored (more or less) average for the field over 9 past years.

All this is based on a called WDVI (Weighted Difference Vegetation Index) per year over the last 9 years. WDVI represents how well a crop is growing.

![](https://raw.githubusercontent.com/FarmHackNL/FarmHack/master/2016/challengers/vandenborne/data/images/bodemscna_eurofins_example.gif)

The Bodemscout data is donated by @TonvanGastel ([eurofins agro](http://blgg.agroxpertus.nl)).

## Puddles by Alterra
 `risicolocaties_oppervlakkige_afspoeling.geojson` shows where puddles are likely to form on Jacob's plots. It is derived from a watershed analysis based on the Dutch height map and information about the soil. The white lines/areas in the image below indicate larger quantities of water (i.e. streams and puddles).

 ![](https://raw.githubusercontent.com/FarmHackNL/FarmHack/master/2016/challengers/vandenborne/data/images/watershed.png)

 This dataset is contributed by [Jan Clement](https://twitter.com/geo_jan) and Harry Massop of [Alterra](https://www.wageningenur.nl/en/Expertise-Services/Research-Institutes/alterra.htm). See the dataset's [documentation](http://www.wageningenur.nl/nl/Publicatie-details.htm?publicationId=publication-way-343536353534) (Dutch) for more information.
