# Msps

MSP (Managed Service Provider) contains multiple Organizations.

```python
msps_controller = client.msps
```

## Class Name

`MspsController`

## Methods

* [Create Msp](../../doc/controllers/msps.md#create-msp)
* [Delete Msp](../../doc/controllers/msps.md#delete-msp)
* [Get Msp Details](../../doc/controllers/msps.md#get-msp-details)
* [Update Msp](../../doc/controllers/msps.md#update-msp)


# Create Msp

Create MSP account

```python
def create_msp(self,
              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Msp`](../../doc/models/msp.md) | Body, Optional | Request Body |

## Response Type

[`Msp`](../../doc/models/msp.md)

## Example Usage

```python
body = Msp(
    name='MSP'
)

result = msps_controller.create_msp(
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
  "name": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Msps401ErrorException`](../../doc/models/api-v1-msps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Msps403ErrorException`](../../doc/models/api-v1-msps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Msps404ErrorException`](../../doc/models/api-v1-msps-404-error-exception.md) |


# Delete Msp

Deleting MSP removes the MSP and OrgGroup under the MSP as well as all privileges associated with them. It does not remove any Org or Admins

```python
def delete_msp(self,
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

result = msps_controller.delete_msp(msp_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Msps401ErrorException`](../../doc/models/api-v1-msps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Msps403ErrorException`](../../doc/models/api-v1-msps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Msps404ErrorException`](../../doc/models/api-v1-msps-404-error-exception.md) |


# Get Msp Details

Get MSP Detail

```python
def get_msp_details(self,
                   msp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Msp`](../../doc/models/msp.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_controller.get_msp_details(msp_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Msps401ErrorException`](../../doc/models/api-v1-msps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Msps403ErrorException`](../../doc/models/api-v1-msps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Msps404ErrorException`](../../doc/models/api-v1-msps-404-error-exception.md) |


# Update Msp

Update MSP

```python
def update_msp(self,
              msp_id,
              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Msp`](../../doc/models/msp.md) | Body, Optional | Request Body |

## Response Type

[`Msp`](../../doc/models/msp.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Msp(
    name='MSP'
)

result = msps_controller.update_msp(
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
  "name": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Msps401ErrorException`](../../doc/models/api-v1-msps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Msps403ErrorException`](../../doc/models/api-v1-msps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Msps404ErrorException`](../../doc/models/api-v1-msps-404-error-exception.md) |

