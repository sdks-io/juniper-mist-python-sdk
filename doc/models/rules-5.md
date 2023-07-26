
# Rules 5

## Structure

`Rules5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `match_model` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `port_config` | [`dict`](../../doc/models/ap-port-config.md) | Optional | The property key is the interface(s) (e.g. "eth1,eth2") |

## Example (as JSON)

```json
{
  "match_model": "match_model2",
  "name": "name0",
  "port_config": {
    "key0": {
      "additional_vlan_ids": [
        177,
        178
      ],
      "authentication_protocol": "eap-peap",
      "disabled": false,
      "dynamic_vlan": {
        "default_vlan_id": 66,
        "enabled": false,
        "type": "type8",
        "vlans": {
          "key0": "vlans7",
          "key1": "vlans8"
        }
      },
      "enable_mac_auth": false
    },
    "key1": {
      "additional_vlan_ids": [
        178,
        179,
        180
      ],
      "authentication_protocol": "eap-md5",
      "disabled": true,
      "dynamic_vlan": {
        "default_vlan_id": 65,
        "enabled": true,
        "type": "type9",
        "vlans": {
          "key0": "vlans6"
        }
      },
      "enable_mac_auth": true
    }
  }
}
```

