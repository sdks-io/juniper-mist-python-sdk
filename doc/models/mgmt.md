
# Mgmt

management-related properties

## Structure

`Mgmt`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mxtunnel_ids` | `List of uuid\|string` | Optional | list of Mist Tunnels |
| `use_mxtunnel` | `bool` | Optional | whether to use Mist Tunnel for mgmt connectivity,  this takes precedence over use_wxtunnel<br>**Default**: `False` |
| `use_wxtunnel` | `bool` | Optional | whether to use wxtunnel for mgmt connectivity<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "use_mxtunnel": false,
  "use_wxtunnel": false,
  "mxtunnel_ids": [
    "000019b0-0000-0000-0000-000000000000",
    "000019b1-0000-0000-0000-000000000000"
  ]
}
```

