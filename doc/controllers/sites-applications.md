# Sites Applications

```python
sites_applications_controller = client.sites_applications
```

## Class Name

`SitesApplicationsController`

## Methods

* [List Site Apps](../../doc/controllers/sites-applications.md#list-site-apps)
* [Count Site Apps](../../doc/controllers/sites-applications.md#count-site-apps)


# List Site Apps

Get List of Site Applications

```python
def list_site_apps(self,
                  site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1SitesAppsResponse`](../../doc/models/api-v1-sites-apps-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_applications_controller.list_site_apps(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "group": "string",
    "key": "string",
    "name": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesApps401ErrorException`](../../doc/models/api-v1-sites-apps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesApps403ErrorException`](../../doc/models/api-v1-sites-apps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesApps404ErrorException`](../../doc/models/api-v1-sites-apps-404-error-exception.md) |


# Count Site Apps

Count by Distinct Attributes of Applications

```python
def count_site_apps(self,
                   site_id,
                   distinct=None,
                   device_mac=None,
                   app=None,
                   wired=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct16Enum`](../../doc/models/distinct-16-enum.md) | Query, Optional | Default for wireless devices is `ap`. Default for wired devices is `device_mac` |
| `device_mac` | `string` | Query, Optional | MAC of the device |
| `app` | `string` | Query, Optional | Application name |
| `wired` | `string` | Query, Optional | If a device is wired or wireless. Default is False. |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_applications_controller.count_site_apps(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "string",
  "end": 0,
  "limit": 0,
  "percentage": 0,
  "results": [
    {
      "count": 0,
      "property": "string"
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsAppsCount401ErrorException`](../../doc/models/api-v1-sites-stats-apps-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsAppsCount403ErrorException`](../../doc/models/api-v1-sites-stats-apps-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsAppsCount404ErrorException`](../../doc/models/api-v1-sites-stats-apps-count-404-error-exception.md) |

