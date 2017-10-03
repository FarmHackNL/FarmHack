# FarmHack

_FarmhackNL mobiliseert coders, creatieven en domeinexperts op vraagstukken van de boer._

## Mest Hack

*Tijdens de Mest Hack zetten we data en technologie in om mest- en nutriëntenstromen beter in beeld te krijgen. Zo komen we op ideeën om het naleven van het beleid voor boeren en transporteurs eenvoudiger te maken, en met minder administratie. Daarnaast zien we waar handhaving beter kan, om echte ‘cowboys’ aan te pakken. Tenslotte werken we aan hele nieuwe innovatiekansen rond mest.*

Locatie: Dairy Campus, Boksumerdyk 11, Leeuwarden

Gitter chatkanaal: https://gitter.im/FarmHackNL/mesthack

Meer informatie en inschrijving: [FarmHack.nl](http://www.farmhack.nl/activiteiten/mesthack/).

### Challenges

#### Boer

Zijn er kansen voor effectief mestbeleid met de **boer centraal**? 

Weet jij wat een boer kan hebben aan Near-infrared Spectroscopy en andere **sensortechnologie**? Kun je de **mineralencyclus** op een boerenbedrijf in **beeld brengen**, en beschikbaar maken op gebiedsniveau? Heb jij ideeën over hoe **akkerbouw en veehouderij** beter kunnen **samenwerken**, bijvoorbeeld door te werken aan de Kringloopwijzer?

#### Milieu

Kunnen we (near real-time) waterkwaliteit- of bodemdata in agrarische vanggebieden gebruiken om de effecten van maatregelen op het milieu te meten?

Ben jij **IoT expert** en zie jij kansen voor mest en milieu-impact **monitoring op bedrijfsniveau**? Of ben je juist actief in een agrarisch collectief en heb je ideeen over **cooperatieve mestverwerking op gebiedsniveau**?

#### Markt

In Nederland is een **overschot aan mest**, dit betekent dat we te maken hebben met een aanbodgedreven markt. We gaan kijken naar de mogelijkheden voor het ontwikkelen van een **digitale marktplaats voor mest**, waar vraag en aanbod bij elkaar komen en keuzemogelijkheden worden geboden voor specifieke distributie- / transportvormen. 

Heb jij een idee voor een mest app die **peer-to-peer informatie uitwisseling** tussen mestproducenten en grondeigenaren faciliteert en akkerbouwers helpt om gericht mest aan te kopen? Ben jij de **blockchain** held die de landbouw helpt aan een gedistribueerd systeem op basis van verifieerbare datastromen?

#### Handhaving
n Nederland zijn de NVWA en RVO gezamenlijk verantwoordelijk voor een goede naleving van de wet. Het is belangrijk voor zowel de handhaver, als voor de boeren, intermediairs en vervoerders dat deze **handhaving slim, efficiënt en data-driven is**.

Ben jij data scientist en wil jij de overheid helpen om **slimmer gebruik te maken van beschikbare data** op zoek naar relaties en patronen? Ben jij een notification/alert wizzard? Of een visual genius en weet jij hoe je de 10 gekste mesttransporten van 2016 in kaart kan brengen?

#### Uitvoerbaarheid

Welke mogelijkheden biedt het **digitaliseren en automatiseren** van de huidige (papieren) administratie voor **snelle en makkelijke verantwoording**? Biedt de **mestketen van de toekomst** de mogelijkheid om **real-time** te zien welke mest waar geladen wordt?

### Data

#### AgroDataCube

**Beschrijving**

AgroDataCube is een datawarehouse met Open Data gegevens relevant voor agro-productie met de Nederlandse gewaspercelen, van 2012 t/m 2016. Voor deze eerste versie is het data warehouse opgeslagen in het PostGIS RDBMS.

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

**Documentatie**

Zie de [AgroDataCube](https://docs.google.com/document/d/1j0-GYmtpi-l-wJ7tjPTnpDA2f8HSBQNf3EgCApivirM/edit#heading=h.egqqt8k8jc2w) voor de volledige lijst van datasets en combinaties.

Contactpersonen: Rob Knapen (@robknapen op Gitter) en IJke van Randen 

**Gebruik**

De AgroDataCube kan direct met SQL of via je favourite programmeertaal benaderd worden. Gebruik QGIS om de data op een kaart te tonen: kies `Layer` -> `Add layer` -> `Add PostGIS Layers...` om de database verbinding te configureren.  

Tijdens de hackathon wordt toegang tot de database verleend.