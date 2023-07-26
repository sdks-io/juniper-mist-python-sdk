# API Token

```python
api_token_controller = client.api_token
```

## Class Name

`APITokenController`

## Methods

* [List Api Tokens](../../doc/controllers/api-token.md#list-api-tokens)
* [Create Api Token](../../doc/controllers/api-token.md#create-api-token)
* [Delete Api Token](../../doc/controllers/api-token.md#delete-api-token)


# List Api Tokens

Get List of Current User API Tokens

```python
def list_api_tokens(self)
```

## Response Type

[`List of Apitoken`](../../doc/models/apitoken.md)

## Example Usage

```python
result = api_token_controller.list_api_tokens()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "key": "string",
    "last_used": 0,
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
          "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
        ]
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SelfApitokens401ErrorException`](../../doc/models/api-v1-self-apitokens-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfApitokens403ErrorException`](../../doc/models/api-v1-self-apitokens-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfApitokens404ErrorException`](../../doc/models/api-v1-self-apitokens-404-error-exception.md) |


# Create Api Token

Create API Token
Note that the key is only available during creation time.

```python
def create_api_token(self,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiV1SelfApitokensRequest`](../../doc/models/api-v1-self-apitokens-request.md) | Body, Optional | - |

## Response Type

[`Apitoken`](../../doc/models/apitoken.md)

## Example Usage

```python
result = api_token_controller.create_api_token()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "key": "string",
  "last_used": 0,
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
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SelfApitokens401ErrorException`](../../doc/models/api-v1-self-apitokens-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfApitokens403ErrorException`](../../doc/models/api-v1-self-apitokens-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfApitokens404ErrorException`](../../doc/models/api-v1-self-apitokens-404-error-exception.md) |


# Delete Api Token

Delete an API Token

```python
def delete_api_token(self,
                    apitoken_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apitoken_id` | `string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
apitoken_id = 'apitoken_id8'

result = api_token_controller.delete_api_token(apitoken_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SelfApitokens401ErrorException`](../../doc/models/api-v1-self-apitokens-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfApitokens403ErrorException`](../../doc/models/api-v1-self-apitokens-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfApitokens404ErrorException`](../../doc/models/api-v1-self-apitokens-404-error-exception.md) |

