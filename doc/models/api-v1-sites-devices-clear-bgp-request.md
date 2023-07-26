
# Api V1 Sites Devices Clear Bgp Request

## Structure

`ApiV1SitesDevicesClearBgpRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `neighbor` | `string` | Required | neighbor ip-address or `all`<br>**Constraints**: *Minimum Length*: `1` |
| `mtype` | [`Type53Enum`](../../doc/models/type-53-enum.md) | Optional | **Default**: `'hard'`<br>**Constraints**: *Minimum Length*: `1` |
| `vrf` | `string` | Optional | vrf name<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "neighbor": "neighbor0",
  "type": "hard",
  "vrf": "vrf4"
}
```

