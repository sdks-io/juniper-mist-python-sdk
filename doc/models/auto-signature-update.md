
# Auto Signature Update

## Structure

`AutoSignatureUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `day_of_week` | `string` | Optional | optional, daily if omitted |
| `enable` | `bool` | Optional | **Default**: `True` |
| `time_of_day` | `string` | Optional | optional, Mist will decide the timing |

## Example (as JSON)

```json
{
  "enable": true,
  "day_of_week": "day_of_week0",
  "time_of_day": "time_of_day6"
}
```

