
# Api V1 Sites Devices Ha Request 1

## Structure

`ApiV1SitesDevicesHaRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mac` | `string` | Optional | when `op` ==`replacement_nodeX`, new node1<br>'s MAC, the device has to be standalone and assigned to the same site |
| `op` | [`Op4Enum`](../../doc/models/op-4-enum.md) | Required | **Default**: `'swap'`<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "op": "swap",
  "mac": "mac4"
}
```

