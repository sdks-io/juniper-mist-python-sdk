
# Api V1 Sites Devices Vc Vc Port Request

## Structure

`ApiV1SitesDevicesVcVcPortRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `members` | [`List of Member2`](../../doc/models/member-2.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `op` | [`Op5Enum`](../../doc/models/op-5-enum.md) | Required | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "members": [
    {
      "member": 116.5,
      "vc_ports": [
        "vc_ports2"
      ]
    }
  ],
  "op": "set"
}
```

