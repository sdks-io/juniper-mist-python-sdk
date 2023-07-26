
# Api V1 Sites Devices Restart Request

## Structure

`ApiV1SitesDevicesRestartRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List of uuid\|string` | Required | - |
| `node` | `string` | Optional | only for SSR: if node is not present, both nodes are restarted<br>for other devices: node should not be present |

## Example (as JSON)

```json
{
  "device_ids": [
    "00001deb-0000-0000-0000-000000000000",
    "00001dec-0000-0000-0000-000000000000"
  ],
  "node": "node2"
}
```

