# Sites Services

```python
sites_services_controller = client.sites_services
```

## Class Name

`SitesServicesController`


# List Site Services Derived

Retrieves the list of Services available for the Site

```python
def list_site_services_derived(self,
                              site_id,
                              resolve=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `resolve` | `bool` | Query, Optional | whether resolve the site variables<br>**Default**: `False` |

## Response Type

[`List of Service`](../../doc/models/service.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

resolve = False

result = sites_services_controller.list_site_services_derived(
    site_id,
    resolve
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "addresses": [
      "string"
    ],
    "apps": [
      "string"
    ],
    "dscp_class": "string",
    "hostnames": [
      "string"
    ],
    "max_jitter": 0,
    "max_latency": "string",
    "max_loss": 0,
    "name": "string",
    "specs": [
      {
        "port_range": "0",
        "protocol": "any"
      }
    ],
    "traffic_class": "best_effort",
    "traffic_type": "default",
    "type": "custom",
    "vpn_name": "addresses"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesServicesDerived401ErrorException`](../../doc/models/api-v1-sites-services-derived-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesServicesDerived403ErrorException`](../../doc/models/api-v1-sites-services-derived-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesServicesDerived404ErrorException`](../../doc/models/api-v1-sites-services-derived-404-error-exception.md) |

