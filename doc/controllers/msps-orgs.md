# Msps Orgs

```python
msps_orgs_controller = client.msps_orgs
```

## Class Name

`MspsOrgsController`

## Methods

* [List Msp Orgs](../../doc/controllers/msps-orgs.md#list-msp-orgs)
* [Create Msp Org](../../doc/controllers/msps-orgs.md#create-msp-org)
* [Manage Msp Orgs](../../doc/controllers/msps-orgs.md#manage-msp-orgs)
* [Search Msp Orgs](../../doc/controllers/msps-orgs.md#search-msp-orgs)
* [Get Msp Org](../../doc/controllers/msps-orgs.md#get-msp-org)


# List Msp Orgs

Get List of MSP Orgs

```python
def list_msp_orgs(self,
                 msp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Org`](../../doc/models/org.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_orgs_controller.list_msp_orgs(msp_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "alarmtemplate_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "allow_mist": true,
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "modified_time": 0,
    "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "name": "string",
    "orggroup_ids": [
      "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
    ],
    "session_expiry": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrgs401ErrorException`](../../doc/models/api-v1-msps-orgs-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrgs403ErrorException`](../../doc/models/api-v1-msps-orgs-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrgs404ErrorException`](../../doc/models/api-v1-msps-orgs-404-error-exception.md) |


# Create Msp Org

Create an Org under MSP

```python
def create_msp_org(self,
                  msp_id,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Org`](../../doc/models/org.md) | Body, Optional | Request Body |

## Response Type

[`Org`](../../doc/models/org.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Org(
    name='string',
    alarmtemplate_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    allow_mist=True,
    orggroup_ids=[
        'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
    ],
    session_expiry=10
)

result = msps_orgs_controller.create_msp_org(
    msp_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "alarmtemplate_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "allow_mist": true,
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "name": "string",
  "orggroup_ids": [
    "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  ],
  "session_expiry": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrgs401ErrorException`](../../doc/models/api-v1-msps-orgs-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrgs403ErrorException`](../../doc/models/api-v1-msps-orgs-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrgs404ErrorException`](../../doc/models/api-v1-msps-orgs-404-error-exception.md) |


# Manage Msp Orgs

Assign or Unassign Orgs to an MSP account

```python
def manage_msp_orgs(self,
                   msp_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1MspsOrgsRequest`](../../doc/models/api-v1-msps-orgs-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1MspsOrgsRequest(
    op=Op3Enum.ASSIGN,
    org_ids=[
        '2b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
    ]
)

result = msps_orgs_controller.manage_msp_orgs(
    msp_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrgs401ErrorException`](../../doc/models/api-v1-msps-orgs-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrgs403ErrorException`](../../doc/models/api-v1-msps-orgs-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrgs404ErrorException`](../../doc/models/api-v1-msps-orgs-404-error-exception.md) |


# Search Msp Orgs

Search Org in MSP

```python
def search_msp_orgs(self,
                   msp_id,
                   name=None,
                   org_id=None,
                   sub_insufficient=None,
                   trial_enabled=None,
                   usage_types=None,
                   limit=100)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `name` | `string` | Query, Optional | - |
| `org_id` | `uuid\|string` | Query, Optional | org id |
| `sub_insufficient` | `bool` | Query, Optional | if this org has sufficient subscription |
| `trial_enabled` | `bool` | Query, Optional | if this org is under trial period |
| `usage_types` | `List of string` | Query, Optional | a list of types that enabled by usage |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |

## Response Type

[`OrgsSearch`](../../doc/models/orgs-search.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

result = msps_orgs_controller.search_msp_orgs(
    msp_id,
    limit
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1614383378.4365287,
  "limit": 10,
  "results": [
    {
      "msp_id": "d287e62f-0000-0000-0000-f2b9ba0a531f",
      "name": "Test Org",
      "num_aps": 9,
      "num_sites": 5,
      "num_switches": 1,
      "num_unassigned_aps": 1,
      "org_id": "bb1a8bf6-0000-0000-0000-8053a663cf65",
      "sub_ana_required": 9,
      "sub_ast_entitled": 5,
      "sub_ast_required": 3,
      "sub_eng_required": 3,
      "sub_ex12_required": 1,
      "sub_insufficient": true,
      "sub_man_required": 9,
      "sub_vna_entitled": 1,
      "timestamp": 1614322563.513937,
      "trial_enabled": false,
      "usage_types": [
        "sub_eng"
      ]
    },
    {
      "msp_id": "d287e62f-0000-0000-0000-f2b9ba0a531f",
      "name": "Rogue Test1",
      "num_aps": 1,
      "num_sites": 1,
      "org_id": "0fb81690-0000-0000-0000-9596d1d1534f",
      "sub_ana_entitled": 1,
      "sub_ana_required": 1,
      "sub_insufficient": false,
      "sub_man_entitled": 1,
      "sub_man_required": 1,
      "timestamp": 1614309876.500955
    }
  ],
  "start": 1613778578.4365668,
  "total": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrgsSearch401ErrorException`](../../doc/models/api-v1-msps-orgs-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrgsSearch403ErrorException`](../../doc/models/api-v1-msps-orgs-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrgsSearch404ErrorException`](../../doc/models/api-v1-msps-orgs-search-404-error-exception.md) |


# Get Msp Org

Get MSP Org Details

```python
def get_msp_org(self,
               msp_id,
               org_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `org_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Org`](../../doc/models/org.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_orgs_controller.get_msp_org(
    msp_id,
    org_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "alarmtemplate_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "allow_mist": true,
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "name": "string",
  "orggroup_ids": [
    "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  ],
  "session_expiry": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrgs401ErrorException`](../../doc/models/api-v1-msps-orgs-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrgs403ErrorException`](../../doc/models/api-v1-msps-orgs-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrgs404ErrorException`](../../doc/models/api-v1-msps-orgs-404-error-exception.md) |

