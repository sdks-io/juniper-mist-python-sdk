
# Mxedge Das

configure cloud-assisted dynamic authorization service on this cluster of mist edges

## Structure

`MxedgeDas`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coa_servers` | [`List of CoaServer1`](../../doc/models/coa-server-1.md) | Optional | dynamic authorization clients configured to send CoA\|DM to mist edges on port 3799 |
| `enabled` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "enabled": false,
  "coa_servers": [
    {
      "disable_event_timestamp_check": false,
      "enabled": false,
      "host": "host6",
      "port": 154,
      "secret": "secret0"
    }
  ]
}
```

