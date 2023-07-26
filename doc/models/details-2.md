
# Details 2

## Structure

`Details2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `major_versions` | [`List of MajorVersion`](../../doc/models/major-version.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `total_switch_count` | `int` | Required | - |

## Example (as JSON)

```json
{
  "major_versions": [
    {
      "major_count": 118.92,
      "model": "model0",
      "system_names": [
        "system_names0"
      ]
    }
  ],
  "total_switch_count": 64
}
```

