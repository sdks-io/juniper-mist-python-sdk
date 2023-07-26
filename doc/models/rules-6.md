
# Rules 6

## Structure

`Rules6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_property` | `string` | Optional | Property key is `match_name[x:y]`, where x and y are the first and the last characters of the string to match. Value is the string to match. |
| `match_model` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `port_config` | [`dict`](../../doc/models/port-config-1.md) | Optional | Object key is a comma separated list of interface names or interface ranges (e.g. ge-0/0/0, ge-0/0/0-5) |

## Example (as JSON)

```json
{
  "additionalProperty": "additionalProperty6",
  "match_model": "match_model2",
  "name": "name0",
  "port_config": {
    "key0": {
      "usage": "usage2"
    },
    "key1": {
      "usage": "usage3"
    }
  }
}
```

