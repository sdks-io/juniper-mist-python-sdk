
# Junos Acl Tags

## Structure

`JunosAclTags`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gbp_tag` | `float` | Optional | required if<br><br>- `type`==`dynamic_gbp` (gbp_tag received from RADIUS)<br>- `type`==`static_gbp` (applying gbp tag against matching conditions) |
| `macs` | `List of string` | Optional | required if<br><br>- `type`==`mac`<br>- `type`==`static_gbp` if from matching mac |
| `network` | `string` | Optional | if:<br><br>- `type`==`mac` (optional. default is `any`)<br>- `type`==`subnet` (optional. default is `any`)<br>- `type`==`network`<br>- `type`==`resource` (optional. default is `any`)<br>- `type`==`static_gbp` if from matching network (vlan) |
| `radius_group` | `string` | Optional | required if<br><br>- `type`==`radius_group`<br>- `type`==`static_gbp` if from matching radius_group |
| `specs` | [`List of Spec`](../../doc/models/spec.md) | Optional | if `type`==`resource`<br>empty means unrestricted, i.e. any |
| `subnets` | `List of string` | Optional | if<br><br>- `type`==`subnet`<br>- `type`==`resource` (optional. default is `any`)<br>- `type`==`static_gbp` if from matching subnet |
| `mtype` | [`Type24Enum`](../../doc/models/type-24-enum.md) | Required | - |

## Example (as JSON)

```json
{
  "gbp_tag": 160.84,
  "macs": [
    "macs5",
    "macs6"
  ],
  "network": "network4",
  "radius_group": "radius_group4",
  "specs": [
    {
      "port_range": 90,
      "protocol": "protocol2"
    },
    {
      "port_range": 91,
      "protocol": "protocol3"
    }
  ],
  "type": "dynamic_gbp"
}
```

