# Msps Org Groups

```python
msps_org_groups_controller = client.msps_org_groups
```

## Class Name

`MspsOrgGroupsController`

## Methods

* [List Msp Org Groups](../../doc/controllers/msps-org-groups.md#list-msp-org-groups)
* [Create Msp Org Group](../../doc/controllers/msps-org-groups.md#create-msp-org-group)
* [Delete Msp Org Group](../../doc/controllers/msps-org-groups.md#delete-msp-org-group)
* [Get Msp Org Group](../../doc/controllers/msps-org-groups.md#get-msp-org-group)
* [Update Msp Org Group](../../doc/controllers/msps-org-groups.md#update-msp-org-group)
* [Search Msp Org Group](../../doc/controllers/msps-org-groups.md#search-msp-org-group)


# List Msp Org Groups

Get List of MSP Org Groups

```python
def list_msp_org_groups(self,
                       msp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Orggroup`](../../doc/models/orggroup.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_org_groups_controller.list_msp_org_groups(msp_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "modified_time": 0,
    "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "name": "string",
    "org_ids": [
      "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrggroups401ErrorException`](../../doc/models/api-v1-msps-orggroups-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrggroups403ErrorException`](../../doc/models/api-v1-msps-orggroups-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrggroups404ErrorException`](../../doc/models/api-v1-msps-orggroups-404-error-exception.md) |


# Create Msp Org Group

Create MSP Org Group

```python
def create_msp_org_group(self,
                        msp_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Orggroup`](../../doc/models/orggroup.md) | Body, Optional | Request Body |

## Response Type

[`Orggroup`](../../doc/models/orggroup.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Orggroup(
    name='string',
    msp_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    org_ids=[
        'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
    ]
)

result = msps_org_groups_controller.create_msp_org_group(
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
  "org_ids": [
    "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrggroups401ErrorException`](../../doc/models/api-v1-msps-orggroups-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrggroups403ErrorException`](../../doc/models/api-v1-msps-orggroups-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrggroups404ErrorException`](../../doc/models/api-v1-msps-orggroups-404-error-exception.md) |


# Delete Msp Org Group

Delete MSP Org Group

```python
def delete_msp_org_group(self,
                        msp_id,
                        orggroup_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `orggroup_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

orggroup_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_org_groups_controller.delete_msp_org_group(
    msp_id,
    orggroup_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrggroups401ErrorException`](../../doc/models/api-v1-msps-orggroups-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrggroups403ErrorException`](../../doc/models/api-v1-msps-orggroups-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrggroups404ErrorException`](../../doc/models/api-v1-msps-orggroups-404-error-exception.md) |


# Get Msp Org Group

Get MSP Org Group Details

```python
def get_msp_org_group(self,
                     msp_id,
                     orggroup_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `orggroup_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Orggroup`](../../doc/models/orggroup.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

orggroup_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_org_groups_controller.get_msp_org_group(
    msp_id,
    orggroup_id
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
  "org_ids": [
    "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrggroups401ErrorException`](../../doc/models/api-v1-msps-orggroups-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrggroups403ErrorException`](../../doc/models/api-v1-msps-orggroups-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrggroups404ErrorException`](../../doc/models/api-v1-msps-orggroups-404-error-exception.md) |


# Update Msp Org Group

Update MSP Org Group

```python
def update_msp_org_group(self,
                        msp_id,
                        orggroup_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `orggroup_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Orggroup`](../../doc/models/orggroup.md) | Body, Optional | Request Body |

## Response Type

[`Orggroup`](../../doc/models/orggroup.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

orggroup_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_org_groups_controller.update_msp_org_group(
    msp_id,
    orggroup_id
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
  "org_ids": [
    "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsOrggroups401ErrorException`](../../doc/models/api-v1-msps-orggroups-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsOrggroups403ErrorException`](../../doc/models/api-v1-msps-orggroups-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsOrggroups404ErrorException`](../../doc/models/api-v1-msps-orggroups-404-error-exception.md) |


# Search Msp Org Group

Search in MSP Orgs

```python
def search_msp_org_group(self,
                        msp_id,
                        mtype,
                        q=None,
                        limit=100,
                        start=0,
                        end=0,
                        duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `mtype` | [`Type45Enum`](../../doc/models/type-45-enum.md) | Query, Required | orgs |
| `q` | `string` | Query, Optional | search string |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`OrggroupsSearch`](../../doc/models/orggroups-search.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

mtype = Type45Enum.ORGS

q = 'search'

limit = 100

start = 0

end = 0

duration = '10m'

result = msps_org_groups_controller.search_msp_org_group(
    msp_id,
    mtype,
    q,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "limit": 0,
  "page": 0,
  "results": [
    {
      "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "text": "string",
      "type": "string"
    }
  ],
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSearch401ErrorException`](../../doc/models/api-v1-msps-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSearch403ErrorException`](../../doc/models/api-v1-msps-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSearch404ErrorException`](../../doc/models/api-v1-msps-search-404-error-exception.md) |

