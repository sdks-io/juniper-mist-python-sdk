
# Vc

## Structure

`Vc`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | [`DeviceSwitchVc`](../../doc/models/device-switch-vc.md) | Optional | Virtual Chassis |

## Example (as JSON)

```json
{
  "id": {
    "member": 196,
    "members": [
      {
        "mac": "mac8",
        "member": 18,
        "vc_ports": [
          "vc_ports8"
        ],
        "vc_role": "backup"
      },
      {
        "mac": "mac9",
        "member": 19,
        "vc_ports": [
          "vc_ports7",
          "vc_ports8",
          "vc_ports9"
        ],
        "vc_role": "master"
      }
    ],
    "new-member": 130,
    "op": "remove"
  }
}
```

