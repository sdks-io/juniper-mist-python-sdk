# Orgs Admin

```python
orgs_admin_controller = client.orgs_admin
```

## Class Name

`OrgsAdminController`


# Register New Admin

Register a new admin and his/her org
An email will also be sent to the user with a link to https://manage.mist.com/verify/register?token=:token

```python
def register_new_admin(self,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiV1RegisterRequest`](../../doc/models/api-v1-register-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
body = ApiV1RegisterRequest(
    email='email0',
    first_name='first_name6',
    last_name='last_name4',
    org_name='org_name6',
    password='password0',
    recaptcha='recaptcha0',
    account_only=False,
    allow_mist=False
)

result = orgs_admin_controller.register_new_admin(
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Register401ErrorException`](../../doc/models/api-v1-register-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Register403ErrorException`](../../doc/models/api-v1-register-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Register404ErrorException`](../../doc/models/api-v1-register-404-error-exception.md) |

