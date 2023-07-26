
# Junos Storm Control

Switch storm control

## Structure

`JunosStormControl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `no_broadcast` | `bool` | Optional | whether to disable storm control on broadcast traffic<br>**Default**: `False` |
| `no_multicast` | `bool` | Optional | whether to disable storm control on multicast traffic<br>**Default**: `False` |
| `no_registered_multicast` | `bool` | Optional | whether to disable storm control on registered multicast traffic<br>**Default**: `False` |
| `no_unknown_unicast` | `bool` | Optional | whether to disable storm control on unknown unicast traffic<br>**Default**: `False` |
| `percentage` | `int` | Optional | bandwidth-percentage, configures the storm control level as a percentage of the available bandwidth<br>**Default**: `80`<br>**Constraints**: `>= 0`, `<= 100` |

## Example (as JSON)

```json
{
  "no_broadcast": false,
  "no_multicast": false,
  "no_registered_multicast": false,
  "no_unknown_unicast": false,
  "percentage": 80
}
```

