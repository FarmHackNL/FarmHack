# Vechtdal - Raalte
De grote vraag voor ‘korte keten’ boeren is hoe zij hun producten van de streek, de stad in kunnen krijgen. De logistiek is snel te duur, en als boer heb je niet 1,2,3 het netwerk en de tijd om zelf te vermarkten. De uitdaging bij deze FarmHack is om langs dit spoor prototypes te ontwikkelen. Ook het realiseren van onderscheidend vermogen is van groot belang voor boeren in korte ketens, een aanvullende vraag is daarom hoe technologie bij kan dragen aan het overbrengen van meer inzicht in de productie van je eten.

## Vechtdalproducten
Ilona Lagas is de voorzitter van Vechtdalproducten, een coöperatie in het Overijssels Vechtdal waarin producenten (boeren), bewerkers (bakkers en slagers) en gebruikers in de horeca (restaurants en hotels) zijn verenigd.

### Data: Silk.co API

The Vechtdalproducten producers, processors, consumers (e.g. restaurants and hotels) and their products are managed in Google Drive spreadsheets.

- TODO List of Vecthdalproducten members TODO

- [Example product list of beer brewery De Pauw](https://docs.google.com/spreadsheets/d/1JuJoTajCuGH8BcRFhYOrISqommrYVsxVVfX8TT14Pqk/edit#gid=0)

We've linked these sheets to [Silk.co](https://www.silk.co) to enable easy visualisation, analysis and data retrieval, see http://vechtdal.silk.co

Silk.co has a **RESTful API** that gives you access to the data cards. See the docs at https://developer.silk.co for more information.

TODO: add 2-3 example queries.

## De Zwolse Stadslanderijen

Jos van Leussen is de initiatiefnemer van ‘De Zwolse Stadslanderijen’, een boerenbeheer maatschappij die zich richt op het beheer en gebruik van een deel van de ‘reservegronden woningbouw’: honderden hectaren grond in en rond de stad die ooit bedoeld waren voor woningbouw.

### Data: Crop-R API

De Zwolse Stadslanderijen manage their data in [Crop-R](https://www.crop-r.com). Crop-R has an extensive API that gives access to a.o. the locations and dimensions of all plots, the activities performed on each plot, current and planned crops, etc.

The API lives at [https://www.crop-r.com/api/v1/](https://www.crop-r.com/api/v1). Please note: it is still very much in beta.

**Authentication**

You need an auth token to interact wit the API. First, use the FarmHack account to log into Crop-R at https://www.crop-r.com#show_login. Second, locate the Crop-R session cookie through the `Preferences/Settings` of your favourite browser. E.g. in Chrome you can find it under `Settings - Show advanced settings - Content settings - All cookies and site data`. The auth token is stored in the `sessionid` cookie's `content` field. Attach its value to your API call as follows

    https://www.crop-r.com/api/v1?format=json&sessionid=XXXXX

You can now request plots, the performed actions, planned events and others.

**Retrieve all plots**

Send a `GET` request to `/api/v1/cropfield/` to retrieve all plots.

    curl "https://www.crop-r.com/api/v1/cropfield/?format=json&sessionid=XXXXX"

Response:

```json
{
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 1
  },
  "objects": [
    {
      "id": 165355,
      "crop": 177,
      "geometry": "POLYGON ((4.2928494159090738 52.0829653189524748, ... 4.2928494159090738 52.0829653189524748))",
      "last_modified": "2016-06-29T16:40:57.525850",
      "name": "De Zwolselanderijen",
      "previous_crop": null,
      "registered_area": 1.1719,
      "soil_researches": [],
      "notes": ""
      ...
    },
    {
      "crop": 177,
      "id": 165355,
      "geometry": "POLYGON ((...))"
      ...
    }
  ]
}

```

Note: the geometry is stored as [Well-Known Text](https://en.wikipedia.org/wiki/Well-known_text).

**Retrieve the performed activities on a plot**

Plot activities such as sowing, spraying, inspecting, etc. are maintained in Crop-R `record`s. Each record contains one or more `activities`.

Send a `GET` request to `/api/v1/record/` to retrieve all `record`s:

    curl "https://www.crop-r.com/api/v1/record?format=json&sessionid=XXXXX"

Response:

```json
{
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 2
  },
  "objects": [
    {
      "activities": [
        {
          "theme": 10,
          "type": 1003,
          "attributes": [
            {
              "type": 1001002,
              "value": 5
            }
          ]
        },
        {
          "theme": 11,
          "type": 1004,
          ...
        }
      ],
      "cropfield": 165355,
      "date": "2016-06-29 23:07",
      "duration": "01:00",
      "field_notes": null,
      "id": 284635,
      "observations": [],
      "processing_state": "performed",
      ...
    },
    {
      ...
    }
  ]
}
```

A plot's `id` is stored in the `cropfield` name. You can use it to retrieve a specific plot from `/cropfield/` as

    https://www.crop-r.nl/api/v1/cropfield/165355?format=json&sessionid=XXXXX

**Retrieve the planned activities on a plot**

TODO