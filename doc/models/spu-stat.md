
# Spu Stat

## Structure

`SpuStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cpu` | `float` | Optional | - |
| `memory` | `float` | Optional | - |
| `sessions` | [`Sessions`](../../doc/models/sessions.md) | Optional | - |

## Example (as JSON)

```json
{
  "cpu": 86.26,
  "memory": 29.7,
  "sessions": {
    "current": 243.98,
    "max": 129.38,
    "pending": 182.12,
    "valid": 13.86
  }
}
```

