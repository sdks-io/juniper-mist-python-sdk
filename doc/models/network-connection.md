
# Network Connection

various network connection info for the SDK client (if known, else omitted), with RSSI in dBm, and signal level as

## Structure

`NetworkConnection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mac` | `string` | Required | - |
| `rssi` | `float` | Required | - |
| `signal_level` | `float` | Required | - |
| `mtype` | `string` | Required | - |

## Example (as JSON)

```json
{
  "mac": "mac4",
  "rssi": 2.78,
  "signal_level": 65.24,
  "type": "type0"
}
```

