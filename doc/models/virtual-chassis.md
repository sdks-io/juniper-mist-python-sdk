
# Virtual Chassis

required for preprovisioned Virtual Chassis

## Structure

`VirtualChassis`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `members` | [`List of Member`](../../doc/models/member.md) | Optional | list of Virtual Chassis mem |
| `preprovisioned` | `bool` | Optional | to configure whether the VC is preprovisioned or nonprovisioned<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "preprovisioned": false,
  "members": [
    {
      "mac": "mac8",
      "vc_role": "linecard"
    },
    {
      "mac": "mac9",
      "vc_role": "master"
    }
  ]
}
```

