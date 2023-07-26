# Sites VP Ns

```python
sites_vp_ns_controller = client.sites_vp_ns
```

## Class Name

`SitesVPNsController`


# List Site Vpns Derived

VPN object represents an overlay network where gateways can participate in and optionally expose routes to.

```python
def list_site_vpns_derived(self,
                          site_id,
                          resolve=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `resolve` | `bool` | Query, Optional | whether resolve the site variables<br>**Default**: `False` |

## Response Type

[`List of Vpn`](../../doc/models/vpn.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

resolve = False

result = sites_vp_ns_controller.list_site_vpns_derived(
    site_id,
    resolve
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "name": "string",
    "paths": {
      "property1": {
        "bfd_profile": "broadband",
        "ip": "string"
      },
      "property2": {
        "bfd_profile": "lte",
        "ip": "string"
      }
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesVpnsDerived401ErrorException`](../../doc/models/api-v1-sites-vpns-derived-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesVpnsDerived403ErrorException`](../../doc/models/api-v1-sites-vpns-derived-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesVpnsDerived404ErrorException`](../../doc/models/api-v1-sites-vpns-derived-404-error-exception.md) |

