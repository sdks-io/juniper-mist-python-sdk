
# Cpu Stat 3

CPU/core stats list

## Structure

`CpuStat3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cpus` | [`dict`](../../doc/models/cpus.md) | Optional | - |
| `idle` | `int` | Optional | percentage of Idle, Idle/(Idle + Busy) since last sampling |
| `interrupt` | `int` | Optional | percentage of Interrupt, (Irq + SoftIrq)/(Idle + Busy) since last sampling |
| `system` | `int` | Optional | percentage of System, System/(Idle + Busy) since last sampling |
| `usage` | `int` | Optional | percentage of load, Busy/(Idle + Busy) since last sampling |
| `user` | `int` | Optional | percentage of User, User/(Idle + Busy) since last sampling |

## Example (as JSON)

```json
{
  "cpus": {
    "key0": {
      "idle": 220,
      "interrupt": 76,
      "system": 84,
      "usage": 42,
      "user": 224
    },
    "key1": {
      "idle": 221,
      "interrupt": 77,
      "system": 83,
      "usage": 43,
      "user": 225
    },
    "key2": {
      "idle": 222,
      "interrupt": 78,
      "system": 82,
      "usage": 44,
      "user": 226
    }
  },
  "idle": 216,
  "interrupt": 72,
  "system": 88,
  "usage": 38
}
```

