
# Pwr Config

power related configs

## Structure

`PwrConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `base` | `float` | Optional | additional power to request during negotiating with PSE over PoE, in mW<br>**Default**: `0` |
| `prefer_usb_over_wifi` | `bool` | Optional | whether to enable power out to peripheral, meanwhile will reduce power to wifi (only for AP45 at power mode)<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "base": 0.0,
  "prefer_usb_over_wifi": false
}
```

