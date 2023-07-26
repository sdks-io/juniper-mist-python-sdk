# Msps SSO Roles

```python
msps_sso_roles_controller = client.msps_sso_roles
```

## Class Name

`MspsSSORolesController`

## Methods

* [List Msp Sso Roles](../../doc/controllers/msps-sso-roles.md#list-msp-sso-roles)
* [Create Msp Sso Role](../../doc/controllers/msps-sso-roles.md#create-msp-sso-role)
* [Delete Msp Sso Role](../../doc/controllers/msps-sso-roles.md#delete-msp-sso-role)
* [Update Msp Sso Role](../../doc/controllers/msps-sso-roles.md#update-msp-sso-role)


# List Msp Sso Roles

Get List of MSP SSO Roles

```python
def list_msp_sso_roles(self,
                      msp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Ssorole`](../../doc/models/ssorole.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_sso_roles_controller.list_msp_sso_roles(msp_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsoroles401ErrorException`](../../doc/models/api-v1-msps-ssoroles-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsoroles403ErrorException`](../../doc/models/api-v1-msps-ssoroles-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsoroles404ErrorException`](../../doc/models/api-v1-msps-ssoroles-404-error-exception.md) |


# Create Msp Sso Role

Create MSP Role

```python
def create_msp_sso_role(self,
                       msp_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Ssorole`](../../doc/models/ssorole.md) | Body, Optional | Request Body |

## Response Type

[`Ssorole`](../../doc/models/ssorole.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Ssorole(
    name='name6',
    privileges=[
        Privileges(
            role=RoleEnum.INSTALLER,
            scope=ScopeEnum.MSP
        )
    ]
)

result = msps_sso_roles_controller.create_msp_sso_role(
    msp_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
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
  ],
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsoroles401ErrorException`](../../doc/models/api-v1-msps-ssoroles-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsoroles403ErrorException`](../../doc/models/api-v1-msps-ssoroles-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsoroles404ErrorException`](../../doc/models/api-v1-msps-ssoroles-404-error-exception.md) |


# Delete Msp Sso Role

Delete MSP SSO Roles

```python
def delete_msp_sso_role(self,
                       msp_id,
                       ssorole_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `ssorole_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

ssorole_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_sso_roles_controller.delete_msp_sso_role(
    msp_id,
    ssorole_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsoroles401ErrorException`](../../doc/models/api-v1-msps-ssoroles-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsoroles403ErrorException`](../../doc/models/api-v1-msps-ssoroles-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsoroles404ErrorException`](../../doc/models/api-v1-msps-ssoroles-404-error-exception.md) |


# Update Msp Sso Role

Update SSO Role

```python
def update_msp_sso_role(self,
                       msp_id,
                       ssorole_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `ssorole_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Ssorole`](../../doc/models/ssorole.md) | Body, Optional | Request Body |

## Response Type

[`Ssorole`](../../doc/models/ssorole.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

ssorole_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Ssorole(
    name='name6',
    privileges=[
        Privileges(
            role=RoleEnum.INSTALLER,
            scope=ScopeEnum.MSP
        )
    ]
)

result = msps_sso_roles_controller.update_msp_sso_role(
    msp_id,
    ssorole_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
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
  ],
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsoroles401ErrorException`](../../doc/models/api-v1-msps-ssoroles-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsoroles403ErrorException`](../../doc/models/api-v1-msps-ssoroles-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsoroles404ErrorException`](../../doc/models/api-v1-msps-ssoroles-404-error-exception.md) |

