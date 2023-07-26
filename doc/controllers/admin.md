# Admin

```python
admin_controller = client.admin
```

## Class Name

`AdminController`


# Verify Admin Invite

**Note**: another call to `GET /api/v1/self` is required to see the new set of privileges

```python
def verify_admin_invite(self,
                       token)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token` | `string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
token = 'token6'

result = admin_controller.verify_admin_invite(token)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InviteVerify401ErrorException`](../../doc/models/api-v1-invite-verify-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InviteVerify403ErrorException`](../../doc/models/api-v1-invite-verify-403-error-exception.md) |
| 404 | Not Found | [`ApiV1InviteVerify404ErrorException`](../../doc/models/api-v1-invite-verify-404-error-exception.md) |

