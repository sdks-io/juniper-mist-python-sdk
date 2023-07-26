# Orgs Admins

```python
orgs_admins_controller = client.orgs_admins
```

## Class Name

`OrgsAdminsController`


# Verify Registration

Verify registration

```python
def verify_registration(self,
                       token)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token` | `string` | Template, Required | - |

## Response Type

[`ApiV1RegisterVerifyResponse`](../../doc/models/api-v1-register-verify-response.md)

## Example Usage

```python
token = 'token6'

result = orgs_admins_controller.verify_registration(token)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "return_to": "http://mist.zendesk.com/hc/quickstart.pdf"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Response if verification expired or already registered | [`ApiV1RegisterVerify400ErrorException`](../../doc/models/api-v1-register-verify-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1RegisterVerify401ErrorException`](../../doc/models/api-v1-register-verify-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1RegisterVerify403ErrorException`](../../doc/models/api-v1-register-verify-403-error-exception.md) |
| 404 | Response if secret is invalid | [`ApiV1RegisterVerify404ErrorException`](../../doc/models/api-v1-register-verify-404-error-exception.md) |

