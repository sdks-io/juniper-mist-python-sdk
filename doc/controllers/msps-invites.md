# Msps Invites

```python
msps_invites_controller = client.msps_invites
```

## Class Name

`MspsInvitesController`

## Methods

* [Invite Msp Admin](../../doc/controllers/msps-invites.md#invite-msp-admin)
* [Uninvite Msp Admin](../../doc/controllers/msps-invites.md#uninvite-msp-admin)
* [Update Msp Admin Invite](../../doc/controllers/msps-invites.md#update-msp-admin-invite)


# Invite Msp Admin

Invite MSP Admin

**Note**: An email will also be sent to the user with a link to https://manage.mist.com/verify/invite?token=:token

```python
def invite_msp_admin(self,
                    msp_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Admin`](../../doc/models/admin.md) | Body, Optional | Request Body |

## Response Type

[`Admin`](../../doc/models/admin.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Admin(
    email='user@example.com',
    first_name='string',
    last_name='string',
    privileges=[
        Privileges(
            role=RoleEnum.ADMIN,
            scope=ScopeEnum.ORG,
            msp_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            msp_name='string',
            name='string',
            org_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            org_name='string',
            orggroup_ids=[
                'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
            ],
            site_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            sitegroup_ids=[
                'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
            ]
        )
    ]
)

result = msps_invites_controller.invite_msp_admin(
    msp_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "admin_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "privileges": [
    {
      "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "msp_name": "string",
      "name": "string",
      "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "org_name": "string",
      "orggroup_ids": [
        "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
      ],
      "role": "admin",
      "scope": "org",
      "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "sitegroup_ids": [
        "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsInvites401ErrorException`](../../doc/models/api-v1-msps-invites-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsInvites403ErrorException`](../../doc/models/api-v1-msps-invites-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsInvites404ErrorException`](../../doc/models/api-v1-msps-invites-404-error-exception.md) |


# Uninvite Msp Admin

Delete admin invite

```python
def uninvite_msp_admin(self,
                      msp_id,
                      invite_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `invite_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

invite_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_invites_controller.uninvite_msp_admin(
    msp_id,
    invite_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsInvites401ErrorException`](../../doc/models/api-v1-msps-invites-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsInvites403ErrorException`](../../doc/models/api-v1-msps-invites-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsInvites404ErrorException`](../../doc/models/api-v1-msps-invites-404-error-exception.md) |


# Update Msp Admin Invite

Update MSP admin invite

```python
def update_msp_admin_invite(self,
                           msp_id,
                           invite_id,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `invite_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Admin`](../../doc/models/admin.md) | Body, Optional | Request Body |

## Response Type

[`Admin`](../../doc/models/admin.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

invite_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Admin(
    email='user@example.com',
    first_name='string',
    last_name='string',
    privileges=[
        Privileges(
            role=RoleEnum.ADMIN,
            scope=ScopeEnum.ORG,
            msp_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            msp_name='string',
            name='string',
            org_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            org_name='string',
            orggroup_ids=[
                'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
            ],
            site_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            sitegroup_ids=[
                'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
            ]
        )
    ]
)

result = msps_invites_controller.update_msp_admin_invite(
    msp_id,
    invite_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "admin_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "privileges": [
    {
      "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "msp_name": "string",
      "name": "string",
      "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "org_name": "string",
      "orggroup_ids": [
        "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
      ],
      "role": "admin",
      "scope": "org",
      "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "sitegroup_ids": [
        "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsInvites401ErrorException`](../../doc/models/api-v1-msps-invites-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsInvites403ErrorException`](../../doc/models/api-v1-msps-invites-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsInvites404ErrorException`](../../doc/models/api-v1-msps-invites-404-error-exception.md) |

