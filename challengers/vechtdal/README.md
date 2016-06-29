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

You need to authenticate with the API. Go to https://www.crop-r.com#show_login and login with the FarmHack account. Your auth token is stored in the sessionid cookie. Attach its value to your API call as follows

    https://www.crop-r.com/api/v1?format=json&sessionid=XXXXX

You can now request the plots, the actions performed on them and the planned events.

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
      "crop": 177,
      "farm": 8112,
      "field_attributes": {},
      "geometry": "POLYGON ((4.2928494159090738 52.0829653189524748, ... 4.2928494159090738 52.0829653189524748))",
      "id": 165355,
      "last_modified": "2016-06-29T16:40:57.525850",
      "name": "De Zwolselanderijen",
      "notes": "",
      "plan": 11465,
      "previous_crop": null,
      "registered_area": 1.1719,
      "soil_researches": [],
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

Plot activities such as sowing, spraying, inspecting, etc. are maintained in `record`s. Each record contains one or more `activities`.

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
    }
  ]
}
```

A plot's `id` is stored in the `cropfield` name. You can use to retrieve a specific plot from `/cropfield/` as

    https://www.crop-r.nl/api/v1/cropfield/165355?format=json&sessionid=XXXXX

**Retrieve the planned activities on a plot**

TODO