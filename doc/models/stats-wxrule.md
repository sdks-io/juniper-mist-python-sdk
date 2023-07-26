
# Stats Wxrule

Wxrule statistics

## Structure

`StatsWxrule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | `string` | Required | - |
| `client_mac` | `List of string` | Required | - |
| `dst_allow_wxtags` | `List of string` | Required | - |
| `dst_deny_wxtags` | `List of string` | Required | - |
| `dst_wxtags` | `List of string` | Required | - |
| `name` | `string` | Required | - |
| `order` | `int` | Required | - |
| `src_wxtags` | `List of string` | Required | - |
| `usage` | `object` | Required | - |

## Example (as JSON)

```json
{
  "action": "action2",
  "client_mac": [
    "client_mac2",
    "client_mac3",
    "client_mac4"
  ],
  "dst_allow_wxtags": [
    "dst_allow_wxtags1",
    "dst_allow_wxtags2"
  ],
  "dst_deny_wxtags": [
    "dst_deny_wxtags1",
    "dst_deny_wxtags2"
  ],
  "dst_wxtags": [
    "dst_wxtags0",
    "dst_wxtags1"
  ],
  "name": "name0",
  "order": 32,
  "src_wxtags": [
    "src_wxtags6",
    "src_wxtags7",
    "src_wxtags8"
  ],
  "usage": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

