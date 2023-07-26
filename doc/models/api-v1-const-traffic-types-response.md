
# Api V1 Const Traffic Types Response

## Structure

`ApiV1ConstTrafficTypesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dscp` | `float` | Required | - |
| `failover_policy` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `name` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `traffic_class` | `string` | Required | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "dscp": 61.2,
  "failover_policy": "failover_policy0",
  "name": "name0",
  "traffic_class": "traffic_class8"
}
```

