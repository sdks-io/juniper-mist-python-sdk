
# Device Switch Vc

Virtual Chassis

## Structure

`DeviceSwitchVc`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member` | `int` | Optional | Only if `op`==`renumber` |
| `members` | [`List of Member1`](../../doc/models/member-1.md) | Optional | - |
| `new_member` | `int` | Optional | Only if `op`==`renumber` |
| `op` | [`OpEnum`](../../doc/models/op-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "member": 84,
  "members": [
    {
      "mac": "mac8",
      "member": 130,
      "vc_ports": [
        "vc_ports2"
      ],
      "vc_role": "backup"
    },
    {
      "mac": "mac9",
      "member": 131,
      "vc_ports": [
        "vc_ports1",
        "vc_ports0"
      ],
      "vc_role": "master"
    }
  ],
  "new-member": 18,
  "op": "remove"
}
```

