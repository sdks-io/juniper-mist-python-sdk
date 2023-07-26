
# Aptemplate

## Structure

`Aptemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_matching` | [`ApMatching`](../../doc/models/ap-matching.md) | Required | - |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `wifi` | [`Wifi`](../../doc/models/wifi.md) | Optional | - |

## Example (as JSON)

```json
{
  "ap_matching": {
    "enabled": false,
    "rules": [
      {
        "match_model": "match_model2",
        "name": "name0",
        "port_config": {
          "key0": {
            "additional_vlan_ids": [
              77
            ],
            "authentication_protocol": "pap",
            "disabled": false,
            "dynamic_vlan": {
              "default_vlan_id": 166,
              "enabled": false,
              "type": "type8",
              "vlans": {
                "key0": "vlans7",
                "key1": "vlans8",
                "key2": "vlans9"
              }
            },
            "enable_mac_auth": false
          }
        }
      },
      {
        "match_model": "match_model1",
        "name": "name9",
        "port_config": {
          "key0": {
            "additional_vlan_ids": [
              78,
              79
            ],
            "authentication_protocol": "eap-peap",
            "disabled": true,
            "dynamic_vlan": {
              "default_vlan_id": 165,
              "enabled": true,
              "type": "type9",
              "vlans": {
                "key0": "vlans6",
                "key1": "vlans7"
              }
            },
            "enable_mac_auth": true
          },
          "key1": {
            "additional_vlan_ids": [
              79,
              80,
              81
            ],
            "authentication_protocol": "eap-md5",
            "disabled": false,
            "dynamic_vlan": {
              "default_vlan_id": 164,
              "enabled": false,
              "type": "type0",
              "vlans": {
                "key0": "vlans5"
              }
            },
            "enable_mac_auth": false
          }
        }
      },
      {
        "match_model": "match_model0",
        "name": "name8",
        "port_config": {
          "key0": {
            "additional_vlan_ids": [
              79,
              80,
              81
            ],
            "authentication_protocol": "eap-md5",
            "disabled": false,
            "dynamic_vlan": {
              "default_vlan_id": 164,
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
              80
            ],
            "authentication_protocol": "pap",
            "disabled": true,
            "dynamic_vlan": {
              "default_vlan_id": 163,
              "enabled": true,
              "type": "type1",
              "vlans": {
                "key0": "vlans4",
                "key1": "vlans5",
                "key2": "vlans6"
              }
            },
            "enable_mac_auth": true
          },
          "key2": {
            "additional_vlan_ids": [
              81,
              82
            ],
            "authentication_protocol": "eap-peap",
            "disabled": false,
            "dynamic_vlan": {
              "default_vlan_id": 162,
              "enabled": false,
              "type": "type2",
              "vlans": {
                "key0": "vlans3",
                "key1": "vlans4"
              }
            },
            "enable_mac_auth": false
          }
        }
      }
    ]
  },
  "created_time": 198.3,
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "org_id": "00000ec8-0000-0000-0000-000000000000"
}
```

