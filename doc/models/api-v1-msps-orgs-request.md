
# Api V1 Msps Orgs Request

## Structure

`ApiV1MspsOrgsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `op` | [`Op3Enum`](../../doc/models/op-3-enum.md) | Required | - |
| `org_ids` | `List of string` | Required | list of org_id |

## Example (as JSON)

```json
{
  "op": "assign",
  "org_ids": [
    "org_ids4"
  ]
}
```

