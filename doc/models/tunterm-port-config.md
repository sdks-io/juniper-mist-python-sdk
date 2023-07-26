
# Tunterm Port Config

ethernet port configurations

## Structure

`TuntermPortConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `downstream_ports` | `List of string` | Optional | list of ports to be used for downstream (to AP) purpose |
| `separate_upstream_downstream` | `bool` | Optional | weather to separate upstream / downstream ports. default is false where all ports will be used.<br>**Default**: `False` |
| `upstream_port_vlan_id` | `int` | Optional | native VLAN id for upstream ports<br>**Default**: `1` |
| `upstream_ports` | `List of string` | Optional | list of ports to be used for upstrea purpose (to LAN) |

## Example (as JSON)

```json
{
  "separate_upstream_downstream": false,
  "upstream_port_vlan_id": 30,
  "downstream_ports": [
    "downstream_ports7"
  ],
  "upstream_ports": [
    "upstream_ports2"
  ]
}
```

