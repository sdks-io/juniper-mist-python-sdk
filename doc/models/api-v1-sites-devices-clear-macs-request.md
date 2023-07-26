
# Api V1 Sites Devices Clear Macs Request

## Structure

`ApiV1SitesDevicesClearMacsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ports` | `List of string` | Optional | the ports on which to clear the detected BPDU error, or `["all"]` for all ports |

## Example (as JSON)

```json
{
  "ports": [
    "ports5",
    "ports6"
  ]
}
```

