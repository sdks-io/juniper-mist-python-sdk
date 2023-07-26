# Sites Wx Rules

```python
sites_wx_rules_controller = client.sites_wx_rules
```

## Class Name

`SitesWxRulesController`

## Methods

* [List Site Wx Rules](../../doc/controllers/sites-wx-rules.md#list-site-wx-rules)
* [Create Site Wx Rule](../../doc/controllers/sites-wx-rules.md#create-site-wx-rule)
* [Get Site Wx Rules Derived](../../doc/controllers/sites-wx-rules.md#get-site-wx-rules-derived)
* [Delete Site Wx Rule](../../doc/controllers/sites-wx-rules.md#delete-site-wx-rule)
* [Get Site Wx Rule](../../doc/controllers/sites-wx-rules.md#get-site-wx-rule)
* [Update Site Wx Rule](../../doc/controllers/sites-wx-rules.md#update-site-wx-rule)


# List Site Wx Rules

Get List of Site WxLan Rules

```python
def list_site_wx_rules(self,
                      site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of WxlanRule`](../../doc/models/wxlan-rule.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_rules_controller.list_site_wx_rules(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "action": "allow",
    "blocked_apps": [
      "string"
    ],
    "created_time": 0,
    "dst_allow_wxtags": [
      "string"
    ],
    "dst_deny_wxtags": [
      "string"
    ],
    "enabled": true,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "modified_time": 0,
    "name": "string",
    "order": 0,
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "src_wxtags": [
      "string"
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxrules401ErrorException`](../../doc/models/api-v1-sites-wxrules-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxrules403ErrorException`](../../doc/models/api-v1-sites-wxrules-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxrules404ErrorException`](../../doc/models/api-v1-sites-wxrules-404-error-exception.md) |


# Create Site Wx Rule

Create Site WxLan Rule

```python
def create_site_wx_rule(self,
                       site_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`WxlanRule`](../../doc/models/wxlan-rule.md) | Body, Optional | Request Body |

## Response Type

[`WxlanRule`](../../doc/models/wxlan-rule.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = WxlanRule(
    order=0,
    src_wxtags=[
        'string'
    ],
    action=Action7Enum.ALLOW,
    blocked_apps=[
        'string'
    ],
    dst_allow_wxtags=[
        'string'
    ],
    dst_deny_wxtags=[
        'string'
    ],
    enabled=True
)

result = sites_wx_rules_controller.create_site_wx_rule(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "action": "allow",
  "blocked_apps": [
    "string"
  ],
  "created_time": 0,
  "dst_allow_wxtags": [
    "string"
  ],
  "dst_deny_wxtags": [
    "string"
  ],
  "enabled": true,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "order": 0,
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "src_wxtags": [
    "string"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxrules401ErrorException`](../../doc/models/api-v1-sites-wxrules-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxrules403ErrorException`](../../doc/models/api-v1-sites-wxrules-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxrules404ErrorException`](../../doc/models/api-v1-sites-wxrules-404-error-exception.md) |


# Get Site Wx Rules Derived

Get Site WxLan Rule Derived

```python
def get_site_wx_rules_derived(self,
                             site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of WxlanRule`](../../doc/models/wxlan-rule.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_rules_controller.get_site_wx_rules_derived(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "action": "allow",
    "blocked_apps": [
      "string"
    ],
    "created_time": 0,
    "dst_allow_wxtags": [
      "string"
    ],
    "dst_deny_wxtags": [
      "string"
    ],
    "enabled": true,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "modified_time": 0,
    "name": "string",
    "order": 0,
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "src_wxtags": [
      "string"
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxrulesDerived401ErrorException`](../../doc/models/api-v1-sites-wxrules-derived-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxrulesDerived403ErrorException`](../../doc/models/api-v1-sites-wxrules-derived-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxrulesDerived404ErrorException`](../../doc/models/api-v1-sites-wxrules-derived-404-error-exception.md) |


# Delete Site Wx Rule

Delete Site WxLan Rule

```python
def delete_site_wx_rule(self,
                       site_id,
                       wxrules_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxrules_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxrules_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_rules_controller.delete_site_wx_rule(
    site_id,
    wxrules_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxrules401ErrorException`](../../doc/models/api-v1-sites-wxrules-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxrules403ErrorException`](../../doc/models/api-v1-sites-wxrules-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxrules404ErrorException`](../../doc/models/api-v1-sites-wxrules-404-error-exception.md) |


# Get Site Wx Rule

Get Site WxLan Rule Details

```python
def get_site_wx_rule(self,
                    site_id,
                    wxrules_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxrules_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`WxlanRule`](../../doc/models/wxlan-rule.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxrules_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_rules_controller.get_site_wx_rule(
    site_id,
    wxrules_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "action": "allow",
  "blocked_apps": [
    "string"
  ],
  "created_time": 0,
  "dst_allow_wxtags": [
    "string"
  ],
  "dst_deny_wxtags": [
    "string"
  ],
  "enabled": true,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "order": 0,
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "src_wxtags": [
    "string"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxrules401ErrorException`](../../doc/models/api-v1-sites-wxrules-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxrules403ErrorException`](../../doc/models/api-v1-sites-wxrules-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxrules404ErrorException`](../../doc/models/api-v1-sites-wxrules-404-error-exception.md) |


# Update Site Wx Rule

Update Site WxLan Rule

```python
def update_site_wx_rule(self,
                       site_id,
                       wxrules_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxrules_id` | `uuid\|string` | Template, Required | - |
| `body` | [`WxlanRule`](../../doc/models/wxlan-rule.md) | Body, Optional | Request Body |

## Response Type

[`WxlanRule`](../../doc/models/wxlan-rule.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxrules_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = WxlanRule(
    order=92.4,
    src_wxtags=[
        'src_wxtags2'
    ],
    enabled=True
)

result = sites_wx_rules_controller.update_site_wx_rule(
    site_id,
    wxrules_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "action": "allow",
  "blocked_apps": [
    "string"
  ],
  "created_time": 0,
  "dst_allow_wxtags": [
    "string"
  ],
  "dst_deny_wxtags": [
    "string"
  ],
  "enabled": true,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "order": 0,
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "src_wxtags": [
    "string"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxrules401ErrorException`](../../doc/models/api-v1-sites-wxrules-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxrules403ErrorException`](../../doc/models/api-v1-sites-wxrules-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxrules404ErrorException`](../../doc/models/api-v1-sites-wxrules-404-error-exception.md) |

