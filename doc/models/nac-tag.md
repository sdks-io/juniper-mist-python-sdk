
# Nac Tag

## Structure

`NacTag`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `egress_vlan_names` | `List of string` | Optional | if `type`==`egress_vlan_names`, list of egress vlans to return |
| `gbp_tag` | `int` | Optional | if `type`==`gbp_tag` |
| `id` | `uuid\|string` | Optional | - |
| `match` | [`MatchEnum`](../../doc/models/match-enum.md) | Optional | if `type`==`match`<br>**Constraints**: *Minimum Length*: `1` |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `org_id` | `uuid\|string` | Optional | - |
| `radius_attrs` | `List of string` | Optional | if `type`==`radius_attrs`, user can specify a list of one or more standard attributes in the field "radius_attrs".<br>It is the responsibility of the user to provide a  syntactically correct string, otherwise it may not work as expected.<br>Note that it is allowed to have more than one radius_attrs in the result of a given rule. |
| `radius_group` | `string` | Optional | if `type`==`radius_group` |
| `radius_vendor_attrs` | `List of string` | Optional | if `type`==`radius_vendor_attrs`, user can specify a list of one or more vendor-specific attributes in the field "radius_vendor_attrs".<br>It is the responsibility of the user to provide a  syntactically correct string, otherwise it may not work as expected.<br>Note that it is allowed to have more than one radius_vendor_attrs in the result of a given rule. |
| `session_timeout` | `int` | Optional | if `type`==`session_timeout, in seconds |
| `mtype` | [`Type34Enum`](../../doc/models/type-34-enum.md) | Required | **Constraints**: *Minimum Length*: `1` |
| `values` | `List of string` | Optional | if `type`==`match` |
| `vlan` | `string` | Optional | if `type`==`vlan` |

## Example (as JSON)

```json
{
  "egress_vlan_names": [
    "1vlan-30",
    "1vlan-20",
    "2-vlan10"
  ],
  "name": "name0",
  "radius_attrs": [
    "Idle-Timeout=600",
    "Termination-Action=RADIUS-Request"
  ],
  "radius_vendor_attrs": [
    "PaloAlto-Admin-Role=superuser",
    "PaloAlto-Panorama-Admin-Role=administrator"
  ],
  "session_timeout": 86000,
  "type": "radius_vendor_attrs",
  "created_time": 198.3,
  "gbp_tag": 212,
  "id": "00001770-0000-0000-0000-000000000000",
  "match": "cert_issuer"
}
```

