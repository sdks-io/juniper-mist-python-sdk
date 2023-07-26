
# Api V1 Sites Devices Show Session Request

## Structure

`ApiV1SitesDevicesShowSessionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `node` | [`Node8Enum`](../../doc/models/node-8-enum.md) | Optional | only for |
| `service_name` | `string` | Optional | The exact service name for which to display the active sessions |

## Example (as JSON)

```json
{
  "service_name": "any",
  "node": "node0"
}
```

