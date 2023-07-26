# Sites Guests

```python
sites_guests_controller = client.sites_guests
```

## Class Name

`SitesGuestsController`

## Methods

* [List Site All Guest Authorizations](../../doc/controllers/sites-guests.md#list-site-all-guest-authorizations)
* [Count Site Guest Authorizations](../../doc/controllers/sites-guests.md#count-site-guest-authorizations)
* [Search Site Guest Authorization](../../doc/controllers/sites-guests.md#search-site-guest-authorization)
* [Delete Site Guest Authorization](../../doc/controllers/sites-guests.md#delete-site-guest-authorization)
* [Get Site Guest Authorization](../../doc/controllers/sites-guests.md#get-site-guest-authorization)
* [Update Site Guest Authorization](../../doc/controllers/sites-guests.md#update-site-guest-authorization)


# List Site All Guest Authorizations

Get List of Site Guest Authorizations

```python
def list_site_all_guest_authorizations(self,
                                      site_id,
                                      wlan_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wlan_id` | `string` | Query, Optional | UUID of single or multiple (Comma separated) WLAN under Site `site_id` (to filter by WLAN) |

## Response Type

[`List of Guest`](../../doc/models/guest.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_guests_controller.list_site_all_guest_authorizations(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "authorized": true,
    "authorized_expiring_time": 0,
    "authorized_time": 0,
    "company": "string",
    "email": "user@example.com",
    "field1": "string",
    "field2": "string",
    "field3": "string",
    "field4": "string",
    "mac": "string",
    "minutes": 0,
    "name": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesGuests401ErrorException`](../../doc/models/api-v1-sites-guests-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesGuests403ErrorException`](../../doc/models/api-v1-sites-guests-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesGuests404ErrorException`](../../doc/models/api-v1-sites-guests-404-error-exception.md) |


# Count Site Guest Authorizations

Count Authorized Guest

```python
def count_site_guest_authorizations(self,
                                   site_id,
                                   distinct='auth_method',
                                   page=1,
                                   limit=100,
                                   start=0,
                                   end=0,
                                   duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct12Enum`](../../doc/models/distinct-12-enum.md) | Query, Optional | **Default**: `'auth_method'` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct12Enum.AUTH_METHOD

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_guests_controller.count_site_guest_authorizations(
    site_id,
    distinct,
    page,
    limit,
    start,
    end,
    duration
)
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
| 401 | Unauthorized | [`ApiV1SitesGuestsCount401ErrorException`](../../doc/models/api-v1-sites-guests-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesGuestsCount403ErrorException`](../../doc/models/api-v1-sites-guests-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesGuestsCount404ErrorException`](../../doc/models/api-v1-sites-guests-count-404-error-exception.md) |


# Search Site Guest Authorization

Search Authorized Guest

```python
def search_site_guest_authorization(self,
                                   site_id,
                                   wlan_id=None,
                                   auth_method=None,
                                   ssid=None,
                                   limit=100,
                                   start=0,
                                   end=0,
                                   duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wlan_id` | `string` | Query, Optional | - |
| `auth_method` | `string` | Query, Optional | - |
| `ssid` | `string` | Query, Optional | - |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`GuestsSearch`](../../doc/models/guests-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wlan_id = '00000000-0000-0000-0000-000000000000'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_guests_controller.search_site_guest_authorization(
    site_id,
    wlan_id,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1531862583,
  "limit": 2,
  "next": "/api/v1/sites/8aaba0aa-09cc-44bd-9709-33b98040550c/guests/search?wlan_id=88ffe630-95b8-11e8-b294-346895ed1b7d&end=1531855849.000&limit=2&start=1531776183.0",
  "results": [
    {
      "ap": "5c5b350e0001",
      "auth_method": "passphrase",
      "authorized_expiring_time": 1531810258.186273,
      "authorized_time": 1531782218,
      "company": "mistsystems",
      "email": "user@mistsys.com",
      "name": "john",
      "ssid": "openNet",
      "timestamp": 1531782218
    },
    {
      "ap": "5c5b350e0001",
      "auth_method": "facebook",
      "authorized_expiring_time": 1531810821.145,
      "authorized_time": 1531782632,
      "company": "xyz inc.",
      "email": "cool_user@yahoo.com",
      "name": "John White",
      "ssid": "openNet",
      "timestamp": 1531782632
    }
  ],
  "start": 1531776183,
  "total": 14
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesGuestsSearch401ErrorException`](../../doc/models/api-v1-sites-guests-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesGuestsSearch403ErrorException`](../../doc/models/api-v1-sites-guests-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesGuestsSearch404ErrorException`](../../doc/models/api-v1-sites-guests-search-404-error-exception.md) |


# Delete Site Guest Authorization

Delete Guest Authorization

```python
def delete_site_guest_authorization(self,
                                   site_id,
                                   guest_mac)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `guest_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

guest_mac = '0000000000ab'

result = sites_guests_controller.delete_site_guest_authorization(
    site_id,
    guest_mac
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesGuests401ErrorException`](../../doc/models/api-v1-sites-guests-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesGuests403ErrorException`](../../doc/models/api-v1-sites-guests-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesGuests404ErrorException`](../../doc/models/api-v1-sites-guests-404-error-exception.md) |


# Get Site Guest Authorization

Get Guest Authorization

```python
def get_site_guest_authorization(self,
                                site_id,
                                guest_mac)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `guest_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

[`Guest`](../../doc/models/guest.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

guest_mac = '0000000000ab'

result = sites_guests_controller.get_site_guest_authorization(
    site_id,
    guest_mac
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "authorized": true,
  "authorized_expiring_time": 0,
  "authorized_time": 0,
  "company": "string",
  "email": "user@example.com",
  "field1": "string",
  "field2": "string",
  "field3": "string",
  "field4": "string",
  "mac": "string",
  "minutes": 0,
  "name": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesGuests401ErrorException`](../../doc/models/api-v1-sites-guests-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesGuests403ErrorException`](../../doc/models/api-v1-sites-guests-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesGuests404ErrorException`](../../doc/models/api-v1-sites-guests-404-error-exception.md) |


# Update Site Guest Authorization

Update Guest Authorization

```python
def update_site_guest_authorization(self,
                                   site_id,
                                   guest_mac,
                                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `guest_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |
| `body` | [`Guest`](../../doc/models/guest.md) | Body, Optional | Request Body |

## Response Type

[`Guest`](../../doc/models/guest.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

guest_mac = '0000000000ab'

body = Guest(
    authorized_expiring_time=1480704955,
    authorized_time=1480704355,
    company='abc',
    email='john@abc.com',
    name='John Smith',
    ssid='Guest-SSID',
    wlan_id='6748cfa6-4e12-11e6-9188-0242ac110007'
)

result = sites_guests_controller.update_site_guest_authorization(
    site_id,
    guest_mac,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "authorized": true,
  "authorized_expiring_time": 0,
  "authorized_time": 0,
  "company": "string",
  "email": "user@example.com",
  "field1": "string",
  "field2": "string",
  "field3": "string",
  "field4": "string",
  "mac": "string",
  "minutes": 0,
  "name": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesGuests401ErrorException`](../../doc/models/api-v1-sites-guests-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesGuests403ErrorException`](../../doc/models/api-v1-sites-guests-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesGuests404ErrorException`](../../doc/models/api-v1-sites-guests-404-error-exception.md) |

