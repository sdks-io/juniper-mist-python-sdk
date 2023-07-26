
# Member 1

## Structure

`Member1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mac` | `string` | Optional | same as the mac of device_id. Required if `op`==`add` |
| `member` | `int` | Optional | Required if `op`==`remove`. Optional if `op`==`add` |
| `vc_ports` | `List of string` | Optional | Optional. Only if `op`==`add` |
| `vc_role` | [`VcRole1Enum`](../../doc/models/vc-role-1-enum.md) | Optional | Optional. Only if `op`==`add` |

## Example (as JSON)

```json
{
  "mac": "mac4",
  "member": 84,
  "vc_ports": [
    "vc_ports2",
    "vc_ports3",
    "vc_ports4"
  ],
  "vc_role": "master"
}
```

