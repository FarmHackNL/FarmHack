##1. Percelen

Jacob percelen zijn over een groot verspreid (sommige liggen in Belgie!). Ze komen in alle soorten, maten en vormen voor. Elk perceel heeft een uniek ID nummer, een naam, oppervlakte, gewas, ras, voorgaand gewas en een locatie.

##2. Bodemscan

Een bodemscan meet de elektrische geleidbaarheid en magnetische gevoeligheid van de bodem. Bodemscans geven inzicht in de samenstelling van de bodem en de locaties van droge en natte plekken. Aan de hand hiervan kan de vruchtbaarheid bepaald worden.

Lees meer over de bodemscans op http://www.vandenborneaardappelen.com/nl/361/bodemscannen-bij-van-den-borne-aardappelen

##3. Schaduwkaarten

Van elk perceel worden er schaduwkaarten gemaakt. Deze geven het schaduwverloop van een perceel aan de hand van een aantal categorieen: permanente schaduw, transitieschaduw, etc. Jacob gebruikt deze gegevens om o.a. de gewasdichtheid te bepalen: planten in de schaduw worden verder van elkaar geplant dan planten in de open lucht. 


Lees meer over variabel poten op http://www.vandenborneaardappelen.com/nl/363/variabel-poen-in-schaduwzones

##4. Pootlogs

De zaai- en -pootlogs laten zien hoe machines naar percelen rijden en wat ze daar zaaien. Elk perceel wordt nauwkeurig ingemeten alvorens het gezaaid wordt met een gewas.

##5. Gewassensing

De Fritzmeier Isaria sensor meet de reflectie van het licht dat op een plant valt. Hieruit zijn o.a. de hoeveelheid biomassa en stikstof van een plant te bepalen. Elk meting is voorzien van een nauwkeurige GPS coordinaat. De metingen worden gebruikt om taakkaarten te maken voor het variabel toedienen van mest en/of kunstmest. Het gewas krijgt op deze manier precies wat het nodig heeft en wordt verspilling tegengegaan.

De sensor meet twee waardes:

- IRMI : is een waarde voor de Red-Edge Position (REP). Deze index geeft aan hoeveel stikstof er in de plant aanwezig
is. Aan de hand van deze data kan bepaald worden hoeveel stikstof er nog bij gestrooid moet
worden. Hiervoor worden er taakkaarten van de data gemaakt of wordt er meteen na de
meting variabel vaste of vloeibare kunstmest toegediend.
- IBI : een biomassa index. Deze index geeft weer hoe groen het oppervlakte is, de waarde kan variëren tussen 0 en 1. Als de grond kaal is geeft de sensor 0 en 1 staat voor een sterk en goed groeiend gewas dat heel de grond bedekt heeft.

In het bestand vind je verder de kolommen 

- sprayer : geeft % aan van de ingestelde spuitvloeistof (meestal 100%)
- section staat voor welke sectie deze procenten gelden.

Aan de hand van de metingen kan de machine meteen variabel kunstmest strooien. Als er MAP (Mapping) in de naam van de file staat is er alleen gemeten; als er Pot (Potato) in de naam van de file staat is er gespoten. 

##7. Opbrengstmeting

Beide aardappelrooiers (de Puma 3 en de Puma+) zijn uitgerust met het opbrengstmeting.

De ruwe data in .csv files is als volgt opgebouwd: datum, tijd, positie, kwaliteit gps signaal,
aantal satellieten. Daarna volgen een x en een y in meters.

De volgende kolom is de snelheid van de rooier in km/h, daarna komt het gewicht van de aardappels op het bunkerbandje. Hier moet alleen nog wel het leeggewicht van het bandje afgetrokken worden, dat staat in de volgende kolom. Met de conversie factor wordt gecorrigeerd voor de tijd dat de aardappels onderweg zijn in de machine. Daarna volgen de snelheid van het bunkerbandje in meter per seconde en de werkbreedte van de machine. Dit is drie meter omdat er vier rijen van 75 centimeter gerooid worden.

Nu komen de opbrengsten waar he om gaat, eerst de opbrengst in ton per hectare voor elke positie. Daarna de totale opbrengst in tonnen, dit is de som van alle voorgaande puntmetingen. Verder zijn er nog het aantal gerooide hectares, de opbrengst per punt en de gewerkte tijd in seconden. Daarna volgen het nummer en het gewicht van elke vracht.
Als laatste zijn er gegevens uit de boordcomputer van de rooier opgenomen. Dit zijn het aantal motortoeren (rpm) , benodigd koppel, geleverd koppel, brandstofverbruik in liter per uur, totaal brandstofverbruik in liters. De tractrear is de olie druk van de wielaandrijving van de rooier. Als de grond verdicht is zal het rooien zwaarder gaan en is er meer olie druk nodig, deze parameter kan dus een indicator zijn voor de bodemverdichting.

Lees meer over gewassensing op http://www.vandenborneaardappelen.com/nl/296/gewassensing
