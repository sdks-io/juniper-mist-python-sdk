
# Ap Switch

for people who want to fully control the vlans (advanced)

## Structure

`ApSwitch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | **Default**: `False` |
| `eth_0` | [`ApSwitchSetting`](../../doc/models/ap-switch-setting.md) | Optional | - |
| `eth_1` | [`ApSwitchSetting`](../../doc/models/ap-switch-setting.md) | Optional | - |
| `eth_2` | [`ApSwitchSetting`](../../doc/models/ap-switch-setting.md) | Optional | - |
| `eth_3` | [`ApSwitchSetting`](../../doc/models/ap-switch-setting.md) | Optional | - |
| `module` | [`ApSwitchSetting`](../../doc/models/ap-switch-setting.md) | Optional | - |
| `wds` | [`ApSwitchSetting`](../../doc/models/ap-switch-setting.md) | Optional | - |

## Example (as JSON)

```json
{
  "enabled": false,
  "eth0": {
    "additional_vlan_ids": [
      143
    ],
    "enable_vlan": false,
    "port_vlan_id": {
      "key1": "val1",
      "key2": "val2"
    },
    "vlan_ids": [
      114,
      115,
      116
    ]
  },
  "eth1": {
    "additional_vlan_ids": [
      175
    ],
    "enable_vlan": false,
    "port_vlan_id": {
      "key1": "val1",
      "key2": "val2"
    },
    "vlan_ids": [
      146,
      147,
      148
    ]
  },
  "eth2": {
    "additional_vlan_ids": [
      147
    ],
    "enable_vlan": false,
    "port_vlan_id": {
      "key1": "val1",
      "key2": "val2"
    },
    "vlan_ids": [
      118,
      119,
      120
    ]
  },
  "eth3": {
    "additional_vlan_ids": [
      9,
      10,
      11
    ],
    "enable_vlan": false,
    "port_vlan_id": {
      "key1": "val1",
      "key2": "val2"
    },
    "vlan_ids": [
      236,
      237
    ]
  }
}
```

