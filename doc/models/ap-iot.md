
# Ap Iot

IoT AP settings

## Structure

`ApIot`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `a_1` | [`ApIotOutput`](../../doc/models/ap-iot-output.md) | Optional | IoT output AP settings |
| `a_2` | [`ApIotOutput`](../../doc/models/ap-iot-output.md) | Optional | IoT output AP settings |
| `a_3` | [`ApIotOutput`](../../doc/models/ap-iot-output.md) | Optional | IoT output AP settings |
| `a_4` | [`ApIotOutput`](../../doc/models/ap-iot-output.md) | Optional | IoT output AP settings |
| `di_1` | [`ApIotInput`](../../doc/models/ap-iot-input.md) | Optional | IoT Input AP settings |
| `di_2` | [`ApIotInput`](../../doc/models/ap-iot-input.md) | Optional | IoT Input AP settings |
| `do` | [`ApIotOutput`](../../doc/models/ap-iot-output.md) | Optional | IoT output AP settings |

## Example (as JSON)

```json
{
  "A1": {
    "enabled": false,
    "name": "name0",
    "output": false,
    "pullup": "external",
    "value": 242
  },
  "A2": {
    "enabled": false,
    "name": "name8",
    "output": false,
    "pullup": "none",
    "value": 180
  },
  "A3": {
    "enabled": false,
    "name": "name6",
    "output": false,
    "pullup": "external",
    "value": 118
  },
  "A4": {
    "enabled": false,
    "name": "name8",
    "output": false,
    "pullup": "external",
    "value": 88
  },
  "DI1": {
    "enabled": false,
    "name": "name0",
    "pullup": "external"
  }
}
```

