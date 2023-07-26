
# Ap Port Config 1

## Structure

`ApPortConfig1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model_specific` | [`dict`](../../doc/models/ap-port-config.md) | Optional | the property key is the AP model (e.g "AP32") |

## Example (as JSON)

```json
{
  "model_specific": {
    "key0": {
      "additional_vlan_ids": [
        21,
        22,
        23
      ],
      "authentication_protocol": "eap-md5",
      "disabled": false,
      "dynamic_vlan": {
        "default_vlan_id": 94,
        "enabled": false,
        "type": "type0",
        "vlans": {
          "key0": "vlans5"
        }
      },
      "enable_mac_auth": false
    },
    "key1": {
      "additional_vlan_ids": [
        22
      ],
      "authentication_protocol": "pap",
      "disabled": true,
      "dynamic_vlan": {
        "default_vlan_id": 95,
        "enabled": true,
        "type": "type9",
        "vlans": {
          "key0": "vlans6",
          "key1": "vlans7"
        }
      },
      "enable_mac_auth": true
    }
  }
}
```

