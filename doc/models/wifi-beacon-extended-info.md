
# Wifi Beacon Extended Info

## Structure

`WifiBeaconExtendedInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `frame_ctrl` | `int` | Optional | frame control field of 802.11 header |
| `payload` | `string` | Optional | Extended Info Payload associated with frame |
| `seq_ctrl` | `int` | Optional | sequence control field of 802.11 header |

## Example (as JSON)

```json
{
  "frame_ctrl": 54,
  "payload": "payload6",
  "seq_ctrl": 114
}
```

