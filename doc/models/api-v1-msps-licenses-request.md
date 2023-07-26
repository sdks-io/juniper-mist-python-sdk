
# Api V1 Msps Licenses Request

## Structure

`ApiV1MspsLicensesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dst_org_id` | `string` | Optional | required if `op`==`amend`, destination org id<br>**Constraints**: *Minimum Length*: `1` |
| `notes` | `string` | Optional | required if `op`== `annotate` |
| `op` | [`Op2Enum`](../../doc/models/op-2-enum.md) | Required | **Constraints**: *Minimum Length*: `1` |
| `quantity` | `float` | Optional | required if `op`==`amend` |
| `subscription_id` | `string` | Optional | required if `op`==`unamend` or `op`== `annotate`<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "dst_org_id": "dst_org_id0",
  "notes": "notes0",
  "op": "delete",
  "quantity": 149.16,
  "subscription_id": "subscription_id0"
}
```

