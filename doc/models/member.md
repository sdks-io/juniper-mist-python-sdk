
# Member

## Structure

`Member`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mac` | `string` | Optional | fpc0, same as the mac of device_id |
| `vc_role` | [`VcRoleEnum`](../../doc/models/vc-role-enum.md) | Optional | Both vc_role master and backup will be matched to routing-engine role in Junos preprovisioned VC config |

## Example (as JSON)

```json
{
  "mac": "aff827549235",
  "vc_role": "master"
}
```

