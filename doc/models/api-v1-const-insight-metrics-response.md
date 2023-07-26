
# Api V1 Const Insight Metrics Response

## Structure

`ApiV1ConstInsightMetricsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ctype` | `List of string` | Optional | - |
| `description` | `string` | Optional | - |
| `exampe` | `List of object` | Optional | - |
| `intervals` | [`dict`](../../doc/models/intervals.md) | Optional | Property key is the interval (e.g. 10m, 1h, ...) |
| `keys` | `object` | Optional | - |
| `params` | [`dict`](../../doc/models/params.md) | Optional | Property key is the parameter name |
| `report_duration` | [`dict`](../../doc/models/report-duration.md) | Optional | Property key is the duration (e.g. 1d, 1w, ...) |
| `report_scopes` | `List of string` | Optional | - |
| `scopes` | [`List of Scope1Enum`](../../doc/models/scope-1-enum.md) | Optional | - |
| `sle_baselined` | `bool` | Optional | - |
| `sle_classifiers` | `List of string` | Optional | - |
| `mtype` | `string` | Optional | - |
| `unit` | `string` | Optional | - |
| `values` | `object` | Optional | - |

## Example (as JSON)

```json
{
  "ctype": [
    "ctype8",
    "ctype9",
    "ctype0"
  ],
  "description": "description0",
  "exampe": [
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "intervals": {
    "key0": {
      "interval": 128,
      "max_age": 148
    },
    "key1": {
      "interval": 129,
      "max_age": 149
    },
    "key2": {
      "interval": 130,
      "max_age": 150
    }
  },
  "keys": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

