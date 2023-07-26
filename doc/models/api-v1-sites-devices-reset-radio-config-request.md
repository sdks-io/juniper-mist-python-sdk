
# Api V1 Sites Devices Reset Radio Config Request

## Structure

`ApiV1SitesDevicesResetRadioConfigRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bands` | `List of string` | Required | list of bands |
| `force` | `bool` | Optional | whether to reset those with radio disabled. default is false (i.e. if user intentionally disables a radio, honor it)<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "bands": [
    "bands0",
    "bands1"
  ],
  "force": false
}
```

