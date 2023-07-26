# Sites Licenses

```python
sites_licenses_controller = client.sites_licenses
```

## Class Name

`SitesLicensesController`


# Get Site License Usage

This shows license usage (i.e. needed) based on the features enabled for the site.

```python
def get_site_license_usage(self,
                          site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`GetLicenceUsage`](../../doc/models/get-licence-usage.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_licenses_controller.get_site_license_usage(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "org_entitled": {
    "SUB-LOC": 30,
    "SUB-MAN": 60
  },
  "svna_enabled": false,
  "trial_enabled": false,
  "usages": {
    "SUB-LOC": 30,
    "SUB-MAN": 60
  },
  "vna_enabled": false,
  "wvna_enabled": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLicensesUsages401ErrorException`](../../doc/models/api-v1-sites-licenses-usages-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLicensesUsages403ErrorException`](../../doc/models/api-v1-sites-licenses-usages-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLicensesUsages404ErrorException`](../../doc/models/api-v1-sites-licenses-usages-404-error-exception.md) |

