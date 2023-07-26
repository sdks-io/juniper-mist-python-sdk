
# Session

## Structure

`Session`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `local_sid` | `int` | Optional | remote sessions id (dynamically unless Tunnel is said to be static) |
| `remote_id` | `string` | Optional | WxlanTunnel Remote ID (user-configured) |
| `remote_sid` | `int` | Optional | remote sessions id (dynamically unless Tunnel is said to be static) |
| `state` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "local_sid": 40,
  "remote_id": "remote_id8",
  "remote_sid": 252,
  "state": "state4"
}
```

