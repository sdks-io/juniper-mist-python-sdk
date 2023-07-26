
# Api V1 Sites Devices Support Request

## Structure

`ApiV1SitesDevicesSupportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `info` | [`InfoEnum`](../../doc/models/info-enum.md) | Optional | optional choice: process, outbound-ssh, and full (default)<br>**Default**: `'full'` |
| `node` | `string` | Optional | optional: for SSR, if node is not present, both nodes support files are uploaded |
| `num_messages_files` | `int` | Optional | optional: number of most recent messages files to upload.<br>**Default**: `1`<br>**Constraints**: `>= 1`, `<= 10` |

## Example (as JSON)

```json
{
  "info": "full",
  "num_messages_files": 1,
  "node": "node2"
}
```

