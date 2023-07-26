
# Ap Matching

## Structure

`ApMatching`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | - |
| `rules` | [`List of Rules1`](../../doc/models/rules-1.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "enabled": false,
  "rules": [
    {
      "match_model": "match_model6",
      "name": "name4",
      "port_config": {
        "key0": {
          "additional_vlan_ids": [
            85,
            86
          ],
          "authentication_protocol": "eap-peap",
          "disabled": false,
          "dynamic_vlan": {
            "default_vlan_id": 158,
            "enabled": false,
            "type": "type4",
            "vlans": {
              "key0": "vlans1",
              "key1": "vlans2"
            }
          },
          "enable_mac_auth": false
        },
        "key1": {
          "additional_vlan_ids": [
            86,
            87,
            88
          ],
          "authentication_protocol": "eap-md5",
          "disabled": true,
          "dynamic_vlan": {
            "default_vlan_id": 157,
            "enabled": true,
            "type": "type5",
            "vlans": {
              "key0": "vlans0"
            }
          },
          "enable_mac_auth": true
        }
      }
    }
  ]
}
```

