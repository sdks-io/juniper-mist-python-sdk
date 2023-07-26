
# Api V1 Sites Devices Restart Request 1

## Structure

`ApiV1SitesDevicesRestartRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member` | `string` | Optional | optional for VC member |
| `node` | `string` | Optional | only for SSR: if node is not present, both nodes are restarted<br>for other devices: node should not be present |

## Example (as JSON)

```json
{
  "member": "member6",
  "node": "node2"
}
```

