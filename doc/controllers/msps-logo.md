# Msps Logo

```python
msps_logo_controller = client.msps_logo
```

## Class Name

`MspsLogoController`

## Methods

* [Delete Msp Logo](../../doc/controllers/msps-logo.md#delete-msp-logo)
* [Post Msp Logo](../../doc/controllers/msps-logo.md#post-msp-logo)


# Delete Msp Logo

Delete MSP Logo

```python
def delete_msp_logo(self,
                   msp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_logo_controller.delete_msp_logo(msp_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsLogo401ErrorException`](../../doc/models/api-v1-msps-logo-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsLogo403ErrorException`](../../doc/models/api-v1-msps-logo-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsLogo404ErrorException`](../../doc/models/api-v1-msps-logo-404-error-exception.md) |


# Post Msp Logo

Upload Logo (only for advanced msp tier)

```python
def post_msp_logo(self,
                 msp_id,
                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1MspsLogoRequest`](../../doc/models/api-v1-msps-logo-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_logo_controller.post_msp_logo(msp_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsLogo401ErrorException`](../../doc/models/api-v1-msps-logo-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsLogo403ErrorException`](../../doc/models/api-v1-msps-logo-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsLogo404ErrorException`](../../doc/models/api-v1-msps-logo-404-error-exception.md) |

