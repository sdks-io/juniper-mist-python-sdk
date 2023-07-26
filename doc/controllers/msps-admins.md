# Msps Admins

```python
msps_admins_controller = client.msps_admins
```

## Class Name

`MspsAdminsController`

## Methods

* [List Msp Admins](../../doc/controllers/msps-admins.md#list-msp-admins)
* [Revoke Msp Admin](../../doc/controllers/msps-admins.md#revoke-msp-admin)
* [Get Msp Admin](../../doc/controllers/msps-admins.md#get-msp-admin)
* [Update Msp Admin](../../doc/controllers/msps-admins.md#update-msp-admin)


# List Msp Admins

Get List of MSP Admins

```python
def list_msp_admins(self,
                   msp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Admin`](../../doc/models/admin.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_admins_controller.list_msp_admins(msp_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "admin_id": "456b7016-a916-a4b1-78dd-72b947c152b7",
    "email": "jsmith@mycorp.org",
    "first_name": "Joe",
    "last_name": "Smith",
    "privileges": [
      {
        "role": "admin",
        "scope": "msp"
      },
      {
        "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
        "role": "admin",
        "scope": "org"
      },
      {
        "orggroup_id": "507f1bab-13ba-73e2-f291-2bcb8d1362b0",
        "role": "read",
        "scope": "orggroup"
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsAdmins401ErrorException`](../../doc/models/api-v1-msps-admins-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsAdmins403ErrorException`](../../doc/models/api-v1-msps-admins-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsAdmins404ErrorException`](../../doc/models/api-v1-msps-admins-404-error-exception.md) |


# Revoke Msp Admin

This removes all privileges this admin has against the MSP. This goes deep all the way to the sites

```python
def revoke_msp_admin(self,
                    msp_id,
                    admin_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `admin_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

admin_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_admins_controller.revoke_msp_admin(
    msp_id,
    admin_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsAdmins401ErrorException`](../../doc/models/api-v1-msps-admins-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsAdmins403ErrorException`](../../doc/models/api-v1-msps-admins-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsAdmins404ErrorException`](../../doc/models/api-v1-msps-admins-404-error-exception.md) |


# Get Msp Admin

Get MSP Admins

```python
def get_msp_admin(self,
                 msp_id,
                 admin_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `admin_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Admin`](../../doc/models/admin.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

admin_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_admins_controller.get_msp_admin(
    msp_id,
    admin_id
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
| 401 | Unauthorized | [`ApiV1MspsAdmins401ErrorException`](../../doc/models/api-v1-msps-admins-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsAdmins403ErrorException`](../../doc/models/api-v1-msps-admins-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsAdmins404ErrorException`](../../doc/models/api-v1-msps-admins-404-error-exception.md) |


# Update Msp Admin

Update MSP Admin

```python
def update_msp_admin(self,
                    msp_id,
                    admin_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `admin_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Admin`](../../doc/models/admin.md) | Body, Optional | Request Body |

## Response Type

[`Admin`](../../doc/models/admin.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

admin_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Admin(
    email='user@example.com',
    first_name='string',
    last_name='string',
    admin_id='919c4da0-421a-479a-918d-df80e426d3bf',
    enable_two_factor=True,
    oauth_google=True,
    privileges=[
        Privileges(
            role=RoleEnum.ADMIN,
            scope=ScopeEnum.ORG,
            for_site=True,
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
    ],
    session_expiry=0,
    tags=[
        'string'
    ],
    two_factor_verified=True
)

result = msps_admins_controller.update_msp_admin(
    msp_id,
    admin_id,
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
| 401 | Unauthorized | [`ApiV1MspsAdmins401ErrorException`](../../doc/models/api-v1-msps-admins-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsAdmins403ErrorException`](../../doc/models/api-v1-msps-admins-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsAdmins404ErrorException`](../../doc/models/api-v1-msps-admins-404-error-exception.md) |

