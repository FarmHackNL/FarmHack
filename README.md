# FarmHack

_FarmhackNL mobiliseert coders, creatieven en domeinexperts op vraagstukken van de boer._

# Mest Hack

*Tijdens de Mest Hack zetten we data en technologie in om mest- en nutriëntenstromen beter in beeld te krijgen. Zo komen we op ideeën om het naleven van het beleid voor boeren en transporteurs eenvoudiger te maken, en met minder administratie. Daarnaast zien we waar handhaving beter kan, om echte ‘cowboys’ aan te pakken. Tenslotte werken we aan hele nieuwe innovatiekansen rond mest.*

Locatie: Dairy Campus, Boksumerdyk 11, Leeuwarden

Gitter chatkanaal: https://gitter.im/FarmHackNL/mesthack

Meer informatie en inschrijving: [FarmHack.nl](http://www.farmhack.nl/activiteiten/mesthack/)

Korte beschrijving van de challenges: [onder aan deze pagina](https://github.com/farmhacknl/farmHack#challenges).

## Data

### AgroDataCube (WUR)

AgroDataCube is een datawarehouse met Open Data gegevens relevant voor agro-productie met de Nederlandse gewaspercelen, van 2012 t/m 2016. Voor deze eerste versie is het data warehouse opgeslagen in het PostgreSQL/PostGIS relationele database.

In de AgroDataCube zijn op dit moment de volgende  open en bewerkte gegevens opgenomen 

1. Perceelsgegevens: [Agrarisch Areaal Nederland](https://data.overheid.nl/data/dataset/agrarisch-areaal-nederland-aan) en [Basisregistratie Gewaspercelen](https://data.overheid.nl/data/dataset/basisregistratie-gewaspercelen-brp) (2012-2016)
2. Administratieve regio's
    1. 6-Positie postcodegebieden 2016
    2. Gemeenten 2015
    3. Provincies
3. Hoogtegegevens: Actueel Hoogtebestand Nederland 
4. Bodemgegevens: Bodemkaart 1:250.000 en 1:50.000 waaruit afgeleid: 
    1. grondsoorten
    2. pH
    3. organische stof
    4. C/N ratio
5. Weergegevens: locatie van KNMI meetstations en observatiedata (2012-2016)
6. GroenMonitor-gegevens: NDVI data (2013-2016) waaruit afgeleid: 
    1. gewasgroei-variabelen voor suikerbietpercelen

Een groot aantal van deze datasets zijn met elkaar gecombineerd bijv. de AHN is gecombineerd met het BRP zodat het mogelijk is om de hoogteprofiel van een perceel op te vragen. 

**Gebruik**

Toegang tot de PostgreSQL/PostGIS database wordt tijdens de hackathon verleend.

Gebruik pgAdmin of je favoriete programmeertaal om de AgroDataCube database te bevragen. 

Gebruik QGIS om de data op een kaart te tonen: kies `Layer` -> `Add layer` -> `Add PostGIS Layers...` om de database verbinding te configureren.  

**Documentatie**

Zie de [AgroDataCube](https://docs.google.com/document/d/1j0-GYmtpi-l-wJ7tjPTnpDA2f8HSBQNf3EgCApivirM/edit#heading=h.egqqt8k8jc2w) voor de volledige lijst van datasets en combinaties.

Contactpersonen: Rob Knapen (@robknapen op Gitter) en IJke van Randen 

### KringloopWijzer (WUR)

*De KringloopWijzer is een managementinstrument dat de mineralenefficiëntie op melkveebedrijven in beeld brengt.*

 Door meer inzicht te krijgen in de mineralenkringloop van dier, voer, bodem en mest kunt melkveehouders beter sturen op de benutting van mineralen. Dit kan bijvoorbeeld leiden tot een hogere grasopbrengst, minder mestafvoer en besparingen op ruwvoeraankoop of kunstmestaankoop.

**Gebruik**

Tijdens de hackathon worden de KLWs van een aantal boerderijen voor de jaren 2012 - 2016 beschikbaar gesteld.

**Documentatie**

Een KrinloopWijzer dataset beschrijft [300+ kenmerken](https://github.com/FarmHackNL/FarmHack#kringloopwijzer) [XLS] van een melkveebedrijf. Deze worden gebruikt om de verschillende kringlopen op het bedrijf in [beeld te brengen](http://www.verantwoordeveehouderij.nl/upload_mm/1/f/d/c091e5d4-b99b-4ded-8899-a3852682b6eb_De%20Marke%20KLW%202013.pdf) [PDF]. 

De [Toelichting kengetallen in KringloopWijzer](http://www.verantwoordeveehouderij.nl/upload_mm/4/d/1/c3fd7d0a-bacf-4be7-9e3e-4d237d2ba920_Copy%20of%20omschrijving%20kengetallen%20KLW201609.xlsx) [XLS] document geeft een beknopte beschrijfivng van de KLW kenmerken.

De [KringloopWijzer Handleiding](http://www.verantwoordeveehouderij.nl/upload_mm/7/8/8/8675b6f8-adc6-428f-afcc-37530613d2ea_handleiding%20KringloopWijzer%20januari%202014.pdf) [PDF] beschrijft de invoer, thema's (graasdieren, voorraad, organische en kunstmest, etc.), uitvoer en analyse. 

### Mesttransporten -en overschotten

De Rijksdienst voor Ondernemend Nederland stelt twee datasets ter beschikking, te weten

- mestoverschot op bedrijfsniveau
- transporten van en naar bedrijven

**Gebruik**

De geagregeerde data wordt tijdens de hackathon na ondertekening van een non-disclosure agreement en na toetsing op niet-herleidbaarheid voor de duur van de hackathon beschikbaar gesteld.

Indien aggregeren/anonimiseren onmogelijk blijkt kunnen bewerkingen en analyses op de lokale IT-infrastructuur worden gedaan m.a.w. de laptop van RVO-medewerker.

### Waterkwaliteit in Flevoland (Waterschap Zuiderzeeland)

Het waterschap Zuiderzeeland meet een groot aantal fysisch-chemische eigenschappen van het oppervlaktewater in Flevoland. Wekelijks worden de waarden van o.a. fosfor, stikstof en ammonium gemeten. 

**Gebruik**

Een _voorbeeld_ van de eerste 200 rijen vind je in [waterkwaliteit-flevoland-sample.tsv](https://github.com/FarmHackNL/FarmHack/blob/master/data/flevoland-waterkwaliteit-sample.tsv).
 
_Download_: [alle metingen in periode 2011 - 2016](http://www2.zuiderzeeland.nl/data/gmaps/waterkwaliteit/chemie2004-2016zzl.zip) [ZIP]. 

**Documentatie**

Op [de data portal van Zuiderzeeland](http://zzl.maps.arcgis.com/apps/MapSeries/index.html?appid=7e598d58e26542d38bb57de7fb0893b8) -> `Waterkwaliteit - toestand` vind je achtergrondinformatie over elk gemeten stof en visualisaties van de metingen.

### Bodem, mest en waterkwaliteitsinformatie (NMI)

Het [Nutriënten Management Instituut](https://www.nmi-agro.nl) stelt een grote hoeveelheid data over bodem, mest en waterkwaliteitsinformatie over de belangrijkste nutrienten op agrarische bedrijven.

**Gebruik** 

Tijdens de hackathon wordt toegang tot de datasets verleend. 

**Documentatie**

Elk dataset is voorzien van uitgebreide beschrijving en documentatie.

### Samenstelling van mest (Komeco)

Komeco stelt een dataset beschikbaar met informatie over de samenstelling van mesttransporten: hoeveelheid droog stof, stikstof, fosfaat en kalium.

**Gebruik**

Tijdens de hackathon wordt toegang tot de datasets verleend.

### Precisiebemesting en NIR metingen (Praktijk Centrum voor Precisielandbouw)

Het PCvPL stelt een aantal datasets m.b.t. precisiebemesting en NIR metingen uit het [Plattelandsontwikkelingsprogramma POP3 Brabant 2014-2020](Plattelandsontwikkelingsprogramma POP3 Brabant 2014-2020) beschikbaar.

**Gebruik**

Tijdens de hackathon wordt toegang tot de datasets verleend.

### GPS track van Roelema bemester (DynaLynx)

[GreenDuo-Roelema-bemester.csv](https://github.com/FarmHackNL/FarmHack/blob/master/data/GreenDuo-Roelema-bemester.csv) toont een bemestingsronde van de Roelema bemester. Het bestand bevat informatie over de GPS positie van de bemester en de water- en mestflow. Zie de eerste 200 rijen in het [voorbeeld bestand](https://github.com/FarmHackNL/FarmHack/blob/master/data/GreenDuo-Roelema-bemester_sample.tsv) voor een indruk.

## Challenges

### Boer

Zijn er kansen voor effectief mestbeleid met de **boer centraal**? 

Weet jij wat een boer kan hebben aan Near-infrared Spectroscopy en andere **sensortechnologie**? Kun je de **mineralencyclus** op een boerenbedrijf in **beeld brengen**, en beschikbaar maken op gebiedsniveau? Heb jij ideeën over hoe **akkerbouw en veehouderij** beter kunnen **samenwerken**, bijvoorbeeld door te werken aan de Kringloopwijzer?

### Milieu

Kunnen we (near real-time) waterkwaliteit- of bodemdata in agrarische vanggebieden gebruiken om de effecten van maatregelen op het milieu te meten?

Ben jij **IoT expert** en zie jij kansen voor mest en milieu-impact **monitoring op bedrijfsniveau**? Of ben je juist actief in een agrarisch collectief en heb je ideeen over **cooperatieve mestverwerking op gebiedsniveau**?

### Markt

In Nederland is een **overschot aan mest**, dit betekent dat we te maken hebben met een aanbodgedreven markt. We gaan kijken naar de mogelijkheden voor het ontwikkelen van een **digitale marktplaats voor mest**, waar vraag en aanbod bij elkaar komen en keuzemogelijkheden worden geboden voor specifieke distributie- / transportvormen. 

Heb jij een idee voor een mest app die **peer-to-peer informatie uitwisseling** tussen mestproducenten en grondeigenaren faciliteert en akkerbouwers helpt om gericht mest aan te kopen? Ben jij de **blockchain** held die de landbouw helpt aan een gedistribueerd systeem op basis van verifieerbare datastromen?

### Handhaving
In Nederland zijn de NVWA en RVO gezamenlijk verantwoordelijk voor een goede naleving van de wet. Het is belangrijk voor zowel de handhaver, als voor de boeren, intermediairs en vervoerders dat deze **handhaving slim, efficiënt en data-driven is**.

Ben jij data scientist en wil jij de overheid helpen om **slimmer gebruik te maken van beschikbare data** op zoek naar relaties en patronen? Ben jij een notification/alert wizzard? Of een visual genius en weet jij hoe je de 10 gekste mesttransporten van 2016 in kaart kan brengen?

### Uitvoerbaarheid

Welke mogelijkheden biedt het **digitaliseren en automatiseren** van de huidige (papieren) administratie voor **snelle en makkelijke verantwoording**? Biedt de **mestketen van de toekomst** de mogelijkheid om **real-time** te zien welke mest waar geladen wordt?