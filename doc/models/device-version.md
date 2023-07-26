
# Device Version

## Structure

`DeviceVersion`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | `string` | Required | Device model (as seen in the device stats) |
| `tag` | `string` | Optional | annotation, stable / beta / alpha. Or it can be empty or nothing which is likely a dev build |
| `version` | `string` | Required | firmware version |

## Example (as JSON)

```json
{
  "model": "model2",
  "tag": "tag6",
  "version": "version4"
}
```

