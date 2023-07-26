
# Sessions 1

## Structure

`Sessions1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `local_sid` | `int` | Required | remote sessions id (dynamically unless Tunnel is said to be static) |
| `remote_id` | `string` | Required | WxlanTunnel Remote ID |
| `remote_sid` | `int` | Required | remote sessions id (dynamically unless Tunnel is said to be static) |
| `state` | `string` | Required | - |

## Example (as JSON)

```json
{
  "local_sid": 40,
  "remote_id": "remote_id8",
  "remote_sid": 252,
  "state": "state4"
}
```

