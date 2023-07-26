
# Nac Rule Matching

## Structure

`NacRuleMatching`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_type` | [`AuthType2Enum`](../../doc/models/auth-type-2-enum.md) | Optional | **Default**: `'cert'` |
| `nactags` | `List of string` | Optional | - |
| `port_types` | [`List of PortTypeEnum`](../../doc/models/port-type-enum.md) | Optional | - |
| `site_ids` | `List of uuid\|string` | Optional | list of site ids to match |
| `sitegroup_ids` | `List of uuid\|string` | Optional | list of sitegroup ids to match |
| `vendor` | `List of string` | Optional | list of vendors to match |

## Example (as JSON)

```json
{
  "auth_type": "cert",
  "nactags": [
    "041d5d36-716c-4cfb-4988-3857c6aa14a2",
    "a809a97f-d599-f812-eb8c-c3f84aabf6ba"
  ],
  "port_types": [
    "wired"
  ],
  "site_ids": [
    "bb19fc3e-4124-4b57-80d9-c3f6edce47c4",
    "bb19fc3e-6564-4b57-80d9-c3f6edce47c1"
  ],
  "sitegroup_ids": [
    "bb19fc3e-4124-4b57-80d9-c3f6edce47c4",
    "bb19fc3e-6564-4b57-80d9-c3f6edce47c1"
  ]
}
```

