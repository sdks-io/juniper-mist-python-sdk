
# Version Compliance

## Structure

`VersionCompliance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `details` | [`Details2`](../../doc/models/details-2.md) | Required | - |
| `score` | `float` | Required | - |

## Example (as JSON)

```json
{
  "details": {
    "major_versions": [
      {
        "major_count": 227.22,
        "model": "model0",
        "system_names": [
          "system_names0",
          "system_names1",
          "system_names2"
        ]
      }
    ],
    "total_switch_count": 14
  },
  "score": 147.4
}
```

