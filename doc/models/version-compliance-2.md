
# Version Compliance 2

## Structure

`VersionCompliance2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `details` | [`Details5`](../../doc/models/details-5.md) | Optional | - |
| `score` | `int` | Optional | - |
| `total_switch_count` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "details": {
    "major_versions": [
      {
        "major_count": 194,
        "major_version": "major_version4",
        "model": "model0",
        "system_names": [
          {
            "key1": "val1",
            "key2": "val2"
          },
          {
            "key1": "val1",
            "key2": "val2"
          },
          {
            "key1": "val1",
            "key2": "val2"
          }
        ]
      }
    ]
  },
  "score": 148,
  "total_switch_count": 64
}
```

