# Sites UI Settings

```python
sites_ui_settings_controller = client.sites_ui_settings
```

## Class Name

`SitesUISettingsController`

## Methods

* [Get Site Curd Settings](../../doc/controllers/sites-ui-settings.md#get-site-curd-settings)
* [Create Site Curd Settings](../../doc/controllers/sites-ui-settings.md#create-site-curd-settings)
* [Get Site Derived Curd Setting](../../doc/controllers/sites-ui-settings.md#get-site-derived-curd-setting)
* [Delete Site Curd Setting](../../doc/controllers/sites-ui-settings.md#delete-site-curd-setting)
* [Get Site Curd Setting](../../doc/controllers/sites-ui-settings.md#get-site-curd-setting)
* [Update Site Curd Setting](../../doc/controllers/sites-ui-settings.md#update-site-curd-setting)


# Get Site Curd Settings

CURD site UI settings

```python
def get_site_curd_settings(self,
                          site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of CurdUiSettings`](../../doc/models/curd-ui-settings.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_ui_settings_controller.get_site_curd_settings(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 1508823803,
    "defaultScopeId": "67970e46-4e12-11e6-9188-0242ad112847",
    "defaultScopeType": "site",
    "defaultTimeRange": {
      "end": 1508828400,
      "endDate": "10/23/2017",
      "interval": "1d",
      "name": "This Week",
      "shortName": "thisWeek",
      "start": 1508655600,
      "usePreset": true
    },
    "description": "Description of the databoard",
    "for_site": true,
    "id": "3bdcc7e8-c04d-4512-b4fc-093da9057eb0",
    "isCustomDataboard": true,
    "isScopeLinked": true,
    "isTimeRangeLinked": true,
    "modified_time": 1508823803,
    "name": "New Databoard",
    "org_id": "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9",
    "purpose": "databoard",
    "site_id": "67970e46-4e12-11e6-9188-0242ad112847",
    "tiles": [
      {
        "chartBand": "2.4 ghz",
        "chartColor": "#00B4AD",
        "chartDirection": "tx + rx",
        "chartRankBy": "",
        "chartType": "timeSeries",
        "colspan": 5,
        "column": 1,
        "hideEmptyRows": true,
        "id": "7a9ab38c-cfc3-483d-b51a-0aec571fadc0-j956nurl",
        "metric": {
          "apiName": "client-dhcp-latency"
        },
        "name": "New Analysis",
        "row": 1,
        "rowspan": 2,
        "scopeId": "e0c767834b4c",
        "scopeType": "client",
        "timeRange": {
          "end": 1508823743,
          "endDate": "10/23/2017",
          "interval": "1d",
          "name": "Past 7 Days",
          "shortName": "7d",
          "start": 1508223600,
          "usePreset": true
        },
        "trendType": "line",
        "vizType": "averageTimeSeriesChart"
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesUisettings401ErrorException`](../../doc/models/api-v1-sites-uisettings-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesUisettings403ErrorException`](../../doc/models/api-v1-sites-uisettings-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesUisettings404ErrorException`](../../doc/models/api-v1-sites-uisettings-404-error-exception.md) |


# Create Site Curd Settings

CURD site UI settings

```python
def create_site_curd_settings(self,
                             site_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`CurdUiSettings`](../../doc/models/curd-ui-settings.md) | Body, Optional | Request Body |

## Response Type

[`CurdUiSettings`](../../doc/models/curd-ui-settings.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_ui_settings_controller.create_site_curd_settings(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 1508823803,
  "defaultScopeId": "67970e46-4e12-11e6-9188-0242ad112847",
  "defaultScopeType": "site",
  "defaultTimeRange": {
    "end": 1508828400,
    "endDate": "10/23/2017",
    "interval": "1d",
    "name": "This Week",
    "shortName": "thisWeek",
    "start": 1508655600,
    "usePreset": true
  },
  "description": "Description of the databoard",
  "for_site": true,
  "id": "3bdcc7e8-c04d-4512-b4fc-093da9057eb0",
  "isCustomDataboard": true,
  "isScopeLinked": true,
  "isTimeRangeLinked": true,
  "modified_time": 1508823803,
  "name": "New Databoard",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "purpose": "databoard",
  "site_id": "67970e46-4e12-11e6-9188-0242ad112847",
  "tiles": [
    {
      "chartBand": "2.4 ghz",
      "chartColor": "#00B4AD",
      "chartDirection": "tx + rx",
      "chartRankBy": "",
      "chartType": "timeSeries",
      "colspan": 5,
      "column": 1,
      "hideEmptyRows": true,
      "id": "7a9ab38c-cfc3-483d-b51a-0aec571fadc0-j956nurl",
      "metric": {
        "apiName": "client-dhcp-latency"
      },
      "name": "New Analysis",
      "row": 1,
      "rowspan": 2,
      "scopeId": "e0c767834b4c",
      "scopeType": "client",
      "timeRange": {
        "end": 1508823743,
        "endDate": "10/23/2017",
        "interval": "1d",
        "name": "Past 7 Days",
        "shortName": "7d",
        "start": 1508223600,
        "usePreset": true
      },
      "trendType": "line",
      "vizType": "averageTimeSeriesChart"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesUisettings401ErrorException`](../../doc/models/api-v1-sites-uisettings-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesUisettings403ErrorException`](../../doc/models/api-v1-sites-uisettings-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesUisettings404ErrorException`](../../doc/models/api-v1-sites-uisettings-404-error-exception.md) |


# Get Site Derived Curd Setting

Get both site UI settings(for_site=true) and org UI settings (for_site=false)

```python
def get_site_derived_curd_setting(self,
                                 site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`CurdUiSettings`](../../doc/models/curd-ui-settings.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_ui_settings_controller.get_site_derived_curd_setting(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 1508823803,
  "defaultScopeId": "67970e46-4e12-11e6-9188-0242ad112847",
  "defaultScopeType": "site",
  "defaultTimeRange": {
    "end": 1508828400,
    "endDate": "10/23/2017",
    "interval": "1d",
    "name": "This Week",
    "shortName": "thisWeek",
    "start": 1508655600,
    "usePreset": true
  },
  "description": "Description of the databoard",
  "for_site": true,
  "id": "3bdcc7e8-c04d-4512-b4fc-093da9057eb0",
  "isCustomDataboard": true,
  "isScopeLinked": true,
  "isTimeRangeLinked": true,
  "modified_time": 1508823803,
  "name": "New Databoard",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "purpose": "databoard",
  "site_id": "67970e46-4e12-11e6-9188-0242ad112847",
  "tiles": [
    {
      "chartBand": "2.4 ghz",
      "chartColor": "#00B4AD",
      "chartDirection": "tx + rx",
      "chartRankBy": "",
      "chartType": "timeSeries",
      "colspan": 5,
      "column": 1,
      "hideEmptyRows": true,
      "id": "7a9ab38c-cfc3-483d-b51a-0aec571fadc0-j956nurl",
      "metric": {
        "apiName": "client-dhcp-latency"
      },
      "name": "New Analysis",
      "row": 1,
      "rowspan": 2,
      "scopeId": "e0c767834b4c",
      "scopeType": "client",
      "timeRange": {
        "end": 1508823743,
        "endDate": "10/23/2017",
        "interval": "1d",
        "name": "Past 7 Days",
        "shortName": "7d",
        "start": 1508223600,
        "usePreset": true
      },
      "trendType": "line",
      "vizType": "averageTimeSeriesChart"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesUisettingsDerived401ErrorException`](../../doc/models/api-v1-sites-uisettings-derived-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesUisettingsDerived403ErrorException`](../../doc/models/api-v1-sites-uisettings-derived-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesUisettingsDerived404ErrorException`](../../doc/models/api-v1-sites-uisettings-derived-404-error-exception.md) |


# Delete Site Curd Setting

CURD site UI settings

```python
def delete_site_curd_setting(self,
                            site_id,
                            uisetting_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `uisetting_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

uisetting_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_ui_settings_controller.delete_site_curd_setting(
    site_id,
    uisetting_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesUisettings401ErrorException`](../../doc/models/api-v1-sites-uisettings-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesUisettings403ErrorException`](../../doc/models/api-v1-sites-uisettings-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesUisettings404ErrorException`](../../doc/models/api-v1-sites-uisettings-404-error-exception.md) |


# Get Site Curd Setting

CURD site UI settings

```python
def get_site_curd_setting(self,
                         site_id,
                         uisetting_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `uisetting_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`CurdUiSettings`](../../doc/models/curd-ui-settings.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

uisetting_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_ui_settings_controller.get_site_curd_setting(
    site_id,
    uisetting_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 1508823803,
  "defaultScopeId": "67970e46-4e12-11e6-9188-0242ad112847",
  "defaultScopeType": "site",
  "defaultTimeRange": {
    "end": 1508828400,
    "endDate": "10/23/2017",
    "interval": "1d",
    "name": "This Week",
    "shortName": "thisWeek",
    "start": 1508655600,
    "usePreset": true
  },
  "description": "Description of the databoard",
  "for_site": true,
  "id": "3bdcc7e8-c04d-4512-b4fc-093da9057eb0",
  "isCustomDataboard": true,
  "isScopeLinked": true,
  "isTimeRangeLinked": true,
  "modified_time": 1508823803,
  "name": "New Databoard",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "purpose": "databoard",
  "site_id": "67970e46-4e12-11e6-9188-0242ad112847",
  "tiles": [
    {
      "chartBand": "2.4 ghz",
      "chartColor": "#00B4AD",
      "chartDirection": "tx + rx",
      "chartRankBy": "",
      "chartType": "timeSeries",
      "colspan": 5,
      "column": 1,
      "hideEmptyRows": true,
      "id": "7a9ab38c-cfc3-483d-b51a-0aec571fadc0-j956nurl",
      "metric": {
        "apiName": "client-dhcp-latency"
      },
      "name": "New Analysis",
      "row": 1,
      "rowspan": 2,
      "scopeId": "e0c767834b4c",
      "scopeType": "client",
      "timeRange": {
        "end": 1508823743,
        "endDate": "10/23/2017",
        "interval": "1d",
        "name": "Past 7 Days",
        "shortName": "7d",
        "start": 1508223600,
        "usePreset": true
      },
      "trendType": "line",
      "vizType": "averageTimeSeriesChart"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesUisettings401ErrorException`](../../doc/models/api-v1-sites-uisettings-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesUisettings403ErrorException`](../../doc/models/api-v1-sites-uisettings-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesUisettings404ErrorException`](../../doc/models/api-v1-sites-uisettings-404-error-exception.md) |


# Update Site Curd Setting

CURD site UI settings

```python
def update_site_curd_setting(self,
                            site_id,
                            uisetting_id,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `uisetting_id` | `uuid\|string` | Template, Required | - |
| `body` | [`CurdUiSettings`](../../doc/models/curd-ui-settings.md) | Body, Optional | Request Body |

## Response Type

[`CurdUiSettings`](../../doc/models/curd-ui-settings.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

uisetting_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = CurdUiSettings(
    created_time=0,
    description='string',
    for_site=True,
    id='491f6eca-6276-4993-bfeb-a3cbbbba6f08',
    modified_time=0,
    org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
    purpose='string',
    site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
    default_scope_id='string',
    default_scope_type='string',
    default_time_range=DefaultTimeRange(
        end=0,
        end_date='string',
        interval='string',
        name='string',
        short_name='string',
        start=0,
        use_preset=True
    ),
    is_custom_databoard=True,
    is_scope_linked=True,
    is_time_range_linked=True,
    name='string',
    tiles=[
        Tile(
            chart_band='string',
            chart_color='string',
            chart_direction='string',
            chart_rank_by='string',
            chart_type='string',
            colspan=0,
            column=0,
            hide_empty_rows=True,
            id='string',
            metric=Metric(
                api_name='string'
            ),
            name='string',
            row=0,
            rowspan=0,
            scope_id='string',
            scope_type='string',
            time_range=TimeRange(
                end=0,
                end_date='string',
                interval='string',
                name='string',
                short_name='string',
                start=0,
                use_preset=True
            ),
            trend_type='string',
            viz_type='string'
        )
    ]
)

result = sites_ui_settings_controller.update_site_curd_setting(
    site_id,
    uisetting_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "defaultScopeId": "string",
  "defaultScopeType": "string",
  "defaultTimeRange": {
    "end": 0,
    "endDate": "string",
    "interval": "string",
    "name": "string",
    "shortName": "string",
    "start": 0,
    "usePreset": true
  },
  "description": "string",
  "for_site": true,
  "id": "490f6eca-6276-4993-bfeb-b3cbbbba6f08",
  "isCustomDataboard": true,
  "isScopeLinked": true,
  "isTimeRangeLinked": true,
  "modified_time": 0,
  "name": "string",
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "purpose": "string",
  "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
  "tiles": [
    {
      "chartBand": "string",
      "chartColor": "string",
      "chartDirection": "string",
      "chartRankBy": "string",
      "chartType": "string",
      "colspan": 0,
      "column": 0,
      "hideEmptyRows": true,
      "id": "string",
      "metric": {
        "apiName": "string"
      },
      "name": "string",
      "row": 0,
      "rowspan": 0,
      "scopeId": "string",
      "scopeType": "string",
      "timeRange": {
        "end": 0,
        "endDate": "string",
        "interval": "string",
        "name": "string",
        "shortName": "string",
        "start": 0,
        "usePreset": true
      },
      "trendType": "string",
      "vizType": "string"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesUisettings401ErrorException`](../../doc/models/api-v1-sites-uisettings-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesUisettings403ErrorException`](../../doc/models/api-v1-sites-uisettings-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesUisettings404ErrorException`](../../doc/models/api-v1-sites-uisettings-404-error-exception.md) |

