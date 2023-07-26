
# Version Compliance 1

version compliance score, major version for gateway, type

## Structure

`VersionCompliance1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `major_version` | [`dict`](../../doc/models/major-version-1.md) | Optional | - |
| `score` | `float` | Optional | - |
| `mtype` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "score": 99.9,
  "type": "gateway",
  "major_version": {
    "key0": {
      "major_count": 157,
      "major_version": "major_version9"
    },
    "key1": {
      "major_count": 156,
      "major_version": "major_version8"
    }
  }
}
```

