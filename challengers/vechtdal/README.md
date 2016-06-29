# Vechtdal - Raalte


## Vechtdalproducten
Ilona Lagas is de voorzitter van Vechtdalproducten, een coöperatie in het Overijssels Vechtdal waarin producenten (boeren), bewerkers (bakkers en slagers) en gebruikers in de horeca (restaurants en hotels) zijn verenigd.

### Data

TODO

## De Zwolse Stadslanderijen

Jos van Leussen is de initiatiefnemer van ‘De Zwolse Stadslanderijen’, een boerenbeheer maatschappij die zich richt op het beheer en gebruik van een deel van de ‘reservegronden woningbouw’: honderden hectaren grond in en rond de stad die ooit bedoeld waren voor woningbouw.

### Data

De Zwolse Stadslanderijen manage their data in [Crop-R](https://www.crop-r.com). Crop-R has an extensive API that gives access to a.o. the locations and dimensions of all the plots, the activities performed on each plot, the current and planned crops, etc.

The API lives at [https://www.crop-r.com/api/v1](https://www.crop-r.com/api/v1). Please note: it is still very much in beta.

**Authentication**

You'll need to authneticate in order to use the API. Go to https://www.crop-r.com#show_login and login with the FarmHack account. Your auth token is stored in the sessionid cookie. Attach the value to your API call as follows

    https://www.crop-r.com/api/v1?format=json&sessionid=XXXXX

You can now request the plots, the actions performed on them and the planned events.

**Retrieve all plots**

Send a `GET` request to `/api/v1/cropfield` to retrieve all plots. Note: don't forget to authenticate with your `sessiondid`

    curl "https://www.crop-r.com/api/v1/cropfield/?format=json&sessionid=XXXXX"

**Retrieve more information about a plot**

TODO

**Retroeve the planned activities on a plot**

TODO