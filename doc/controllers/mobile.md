# Mobile

```python
mobile_controller = client.mobile
```

## Class Name

`MobileController`


# Activate Sdk Invite

Verify secret

```python
def activate_sdk_invite(self,
                       secret,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `secret` | `string` | Template, Required | - |
| `body` | [`ModelObjectDeviceId`](../../doc/models/model-object-device-id.md) | Body, Optional | - |

## Response Type

[`ApiV1MobileVerifyResponse`](../../doc/models/api-v1-mobile-verify-response.md)

## Example Usage

```python
secret = 'secret4'

body = ModelObjectDeviceId(
    device_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
)

result = mobile_controller.activate_sdk_invite(
    secret,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "name": "Macy's",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "secret": "device-specific-secret"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MobileVerify401ErrorException`](../../doc/models/api-v1-mobile-verify-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MobileVerify403ErrorException`](../../doc/models/api-v1-mobile-verify-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MobileVerify404ErrorException`](../../doc/models/api-v1-mobile-verify-404-error-exception.md) |

