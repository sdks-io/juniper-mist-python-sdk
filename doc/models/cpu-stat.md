
# Cpu Stat

## Structure

`CpuStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idle` | `float` | Optional | - |
| `interrupt` | `float` | Optional | - |
| `load_avg` | `List of object` | Optional | - |
| `system` | `float` | Optional | - |
| `user` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "idle": 245.36,
  "interrupt": 103.12,
  "load_avg": [
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "system": 126.32,
  "user": 91.8
}
```

