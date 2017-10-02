# Vechtdal - Raalte
De grote vraag voor ‘korte keten’ boeren is hoe zij hun producten van de streek, de stad in kunnen krijgen. De logistiek is snel te duur, en als boer heb je niet 1,2,3 het netwerk en de tijd om zelf te vermarkten. De uitdaging bij deze FarmHack is om langs dit spoor prototypes te ontwikkelen. Ook het realiseren van onderscheidend vermogen is van groot belang voor boeren in korte ketens, een aanvullende vraag is daarom hoe technologie bij kan dragen aan het overbrengen van meer inzicht in de productie van je eten.

## Vechtdalproducten
Ilona Lagas is de voorzitter van Vechtdalproducten, een coöperatie in het Overijssels Vechtdal waarin producenten (boeren), bewerkers (bakkers en slagers) en gebruikers in de horeca (restaurants en hotels) zijn verenigd.

### Data: Silk.co API

The Vechtdalproducten producers, processors, consumers (e.g. restaurants and hotels) and their products are managed in Google Drive spreadsheets.

- [List of Vecthdalproducten members](https://drive.google.com/open?id=1oJGFhMywTM6JKDJ2jOXiie45nCYeYiUNM0A_o46vtt0)

- [Vechtdalproducten product sheets](https://drive.google.com/folderview?id=0BzyupdeOW2PqZHdlcWdqVENlOG8)

- [Example product list of beer brewery De Pauw](https://docs.google.com/spreadsheets/d/1JuJoTajCuGH8BcRFhYOrISqommrYVsxVVfX8TT14Pqk/edit#gid=0)

We've linked these sheets to [Silk.co](https://www.silk.co) to enable easy visualisation, analysis and data retrieval, see http://vechtdal.silk.co

Silk.co has a **RESTful API** that gives you access to the data cards. See the docs at https://developer.silk.co for more information.

TODO: add 2-3 example queries.

## De Zwolse Stadslanderijen

Jos van Leussen is de initiatiefnemer van ‘De Zwolse Stadslanderijen’, een boerenbeheer maatschappij die zich richt op het beheer en gebruik van een deel van de ‘reservegronden woningbouw’: honderden hectaren grond in en rond de stad die ooit bedoeld waren voor woningbouw.

### Data: Crop-R API

De Zwolse Stadslanderijen manage their data in [Crop-R](https://www.crop-r.com). Crop-R has an extensive API that gives access to a.o. the locations and dimensions of all plots, the activities performed on each plot, and information about the current and planned crops.

The API lives at [https://www.crop-r.com/api/v1/](https://www.crop-r.com/api/v1/).

Here be dragons: this is an "internal" API optimized for caching and latency. Crop-R is currently building `v3` which will optimize for developer wellbeing.

#### Authentication

You need an auth token to interact wit the API. The token is stored in the Crop-R session cookie. You can retrieve it as follows

- [log into Crop-R](https://www.crop-r.com#show_login) using the Farm Hack guest account. Send a DM to @ndkv or @AnneFarmHack on [Gitter](https://gitter.im/FarmHackNL/farmhack) to get the credentials.
- locate the Crop-R `sessionid` cookie in your browser. In Chrome you can find it under `Settings - Show advanced settings - Content settings - All cookies and site data`.
- copy your auth token from the cookie's `content` field.

Authenticate your requests by adding the `sessionid=XXXXX` parameters as follows

    https://www.crop-r.com/api/v1?format=json&sessionid=XXXXX

Replace `XXXXX` with the value from your auth token's `content` field. You can now request plots, the performed actions, planned events and others.

#### Retrieve all plots

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
      "id": 165356,
      "geometry": "POLYGON ((...))"
      ...
    }
  ]
}

```

The crops are stored in the `objects` list. Each plot has an `id`, a `crop` type, a `geometry`, a.o.

Note: the geometry is stored as [Well-Known Text](https://en.wikipedia.org/wiki/Well-known_text).

#### Retrieve a crop's name

The crop names are stored in `crop-r_lookup.json`. The `croptype_list` list holds the definitions as

```json
"croptype_list": [
        {
            "id": 100590,
            "category": 58,
            "seed_unit": "eenheden",
            "edi_code": "2060101",
            "name": "1e jaars plantui",
            "color": "#8E388E",
            "default_croppurpose": {...},
            "species": [...],
            "variant": "crop",
            "purposes": [...]
        },
        ...
```

A field's `crop` value from the `api/v1/cropfield` response corresponds to the `id` of a crop from `crop_typelist`. In other words, a field's `crop` value corresponds to `croptype_list[0]["id"]`.

**For example**, to fetch the name of e.g. `crop: 100590` you need to iterate over `croptype_list`, look for `id: 100590` and extract the value of `name`. In the example above this is `1e jaars plantui`.

#### Retrieve the performed activities on a plot

Plot activities such as sowing, spraying, inspecting, harvesting, etc. are maintained in `records`. Each record contains one or more `activities`.

Send a `GET` request to `/api/v1/record/` to retrieve all `records`:

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
          "items": [...]
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
    {...}
  ]
}
```

The `objects` list contains the Crop-R records. Each `record` contains one or more `activities`.

You can also request the records of a single field by adding the`cropfield` parameter as follows

    curl "https://www.crop-r.com/api/v1/record?format=json&cropfield=165394"

#### Retrieve the theme of an activity

As you can see in the response above, activities consist of `themes` and `types`. The `theme` depicts the general category of an activity e.g. crop protection whereas `type` specifies the used method.

The `themes` and `types` definitions are stored in `crop-r_lookup.json`.

`theme` definitions are stored under `default_configuration -> recording -> children -> title` as follows:

```json
"default_configuration": {
    "recording": {
        "category": "data",
        "title": "Registratie configuratie",
        "text": "Stel in welke attributen en methodoen je kan registreren",
        "open_by_default": true,
        "type": "recording",
        "children": [
            {
                "selected": true,
                "key": 4,
                "title": "Grondbewerken",
                "children": [...]
            },
            {
                "selected": true,
                "key": 5,
                "title": "Bereiden teeltbed",
                "children": [...]
            },
            ...
        ]
    }
}
```

The value of an activity's `theme` property in the `/api/v1/record/` response corresponds to the `key` of a `recording`'s child. In other words, an activity's `theme` corresponds to `default_configuration["recording"]["children"][0]["key"]`.

#### Retrieve the type of an activity

The `type` of an activity is stored in `crop-r_lookup.json` as well. It lives in `default_configuration -> recording -> children -> children -> ['title'] = Methods -> children -> title`.

```json
"default_configuration": {
        "recording": {
            "category": "data",
            "title": "Registratie configuratie",
            "text": "Stel in welke attributen en methodoen je kan registreren",
            "open_by_default": true,
            "type": "recording",
            "children": [
                {
                    "selected": true,
                    "key": 4,
                    "title": "Grondbewerken",
                    "children": [
                        {
                            "key": 1000401,
                            "title": "Breedte"
                        },
                        {
                            "key": 1000400,
                            "title": "Diepte"
                        },
                        {
                            "title": "Methodes",
                            "selected": true,
                            "children": [
                                {
                                    "selected": true,
                                    "key": 409,
                                    "title": "Aanaarden"
                                },
```

The value of an activity's `type` property in the `api/v1/record/` response corresponds to the `key` of a Method's child i.e. it corresponds to `default_configuration["recording"]["children]["children"][2]["children]["key"]`

#### HOWTO: convert Well-Known Text geometries to GeoJSON

See [issue #7](https://github.com/FarmHackNL/FarmHack/issues/7) for an example Python conversion script.