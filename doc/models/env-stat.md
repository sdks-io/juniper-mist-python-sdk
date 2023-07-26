
# Env Stat

device environment, including CPU temperature, Ambient temperature, Humidity, Attitude, Pressure, Accelerometers, Magnetometers and vCore Voltage

## Structure

`EnvStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accel_x` | `float` | Optional | - |
| `accel_y` | `float` | Optional | - |
| `accel_z` | `float` | Optional | - |
| `ambient_temp` | `int` | Optional | - |
| `attitude` | `int` | Optional | - |
| `cpu_temp` | `int` | Optional | - |
| `humidity` | `int` | Optional | - |
| `magne_x` | `float` | Optional | - |
| `magne_y` | `float` | Optional | - |
| `magne_z` | `float` | Optional | - |
| `pressure` | `int` | Optional | - |
| `vcore_voltage` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "accel_x": 138.14,
  "accel_y": 237.44,
  "accel_z": 128.18,
  "ambient_temp": 66,
  "attitude": 104
}
```

