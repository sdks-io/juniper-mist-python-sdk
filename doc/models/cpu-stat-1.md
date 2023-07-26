
# Cpu Stat 1

## Structure

`CpuStat1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idle` | `int` | Optional | Percentage of CPU time that is idle |
| `interrupt` | `int` | Optional | Percentage of CPU time being used by interrupts |
| `load_avg` | `List of object` | Optional | Load averages for the last 1, 5, and 15 minutes |
| `system` | `int` | Optional | Percentage of CPU time being used by system processes |
| `user` | `int` | Optional | Percentage of CPU time being used by user processe |

## Example (as JSON)

```json
{
  "idle": 216,
  "interrupt": 72,
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
  "system": 88,
  "user": 220
}
```

