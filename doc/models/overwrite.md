
# Overwrite

## Structure

`Overwrite`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Action2Enum`](../../doc/models/action-2-enum.md) | Optional | - alert (default)<br>- drop: siliently dropping packets<br>- close: notify client/server to close connection<br>**Default**: `'alert'` |
| `matching` | [`Matching`](../../doc/models/matching.md) | Optional | - |

## Example (as JSON)

```json
{
  "action": "alert",
  "matching": {
    "attack_name": [
      "attack_name9"
    ],
    "dst_subnet": [
      "dst_subnet5"
    ],
    "severity": [
      "critical",
      "major"
    ]
  }
}
```

